import streamlit as st
import os
import re
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer
import pandas as pd
import requests
import datetime as dt
import urllib3

warnings.filterwarnings('ignore')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ------------------------------------------------------------------
# Streamlit Page Configuration
# ------------------------------------------------------------------
st.set_page_config(page_title="NeuroPolis Chatbot", layout="wide")

# ------------------------------------------------------------------
# Custom Dark-Themed CSS for a Unified Chat UI
# ------------------------------------------------------------------
st.markdown(
    """
    <style>
    body {
      background-color: #1E1E1E;  
      color: #FFFFFF;
      margin: 0;
      padding: 0;
    }
    header, footer { visibility: hidden; }
    
    .top-right-date {
      position: absolute;
      top: 10px;
      right: 25px;
      color: #AAAAAA;
      font-size: 0.85rem;
    }
    
    /* Chat container styling */
    .chat-container {
      background-color: #2B2B2B;
      padding: 20px;
      border-radius: 8px;
      height: 450px;       /* fixed height so the container doesn't force page scrolling */
      overflow-y: auto;    /* auto-scroll within this container */
      display: flex;
      flex-direction: column;
    }
    .chat-message {
      background-color: #2B2B2B;
      color: #FFFFFF;
      border: 1px solid #4C4C4C;
      padding: 10px;
      border-radius: 5px;
      margin: 5px 0;
      max-width: 75%;
    }
    .user { align-self: flex-end; }
    .bot { align-self: flex-start; }
    
    /* Input area remains fixed at the bottom */
    .input-area {
      position: fixed;
      bottom: 20px;
      width: 90%;
      max-width: 800px;
      left: 50%;
      transform: translateX(-50%);
    }
    
    /* Sidebar customizations for dark theme */
    .css-qri22k, .css-18e3th9 {
      color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

today_str = dt.datetime.now().strftime("%B %d, %Y")
st.markdown(f"<div class='top-right-date'>{today_str}</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Basic Setup & NLTK Configuration
# ------------------------------------------------------------------
os.environ["NLTK_DATA"] = "/root/nltk_data"
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# ------------------------------------------------------------------
# Read Document Content from Local File
# ------------------------------------------------------------------
DOCUMENT_FILENAME = "Corpus_Content.txt"
if os.path.exists(DOCUMENT_FILENAME):
    with open(DOCUMENT_FILENAME, "r", encoding="utf-8") as f:
        raw = f.read().lower()
else:
    raw = "this fallback text is used because no document was found. ask me anything or validate a tweet."

# ------------------------------------------------------------------
# NLTK Tokenization
# ------------------------------------------------------------------
try:
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
except LookupError:
    nltk.download('punkt_tab')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

sent_tokens = tokenizer.tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# ------------------------------------------------------------------
# Zone Extraction Logic
# ------------------------------------------------------------------
def extract_zone_sentences(zone: str, sentences: list) -> str:
    """
    Searches the list of sentences for those containing 'zone <zone>'
    and returns only those sentences concatenated.
    """
    zone_pattern = re.compile(r'\bzone\s*' + re.escape(zone) + r'\b', re.IGNORECASE)
    matches = [s.strip() for s in sentences if zone_pattern.search(s)]
    if matches:
        return "\n".join(matches)
    else:
        return f"No information found for Zone {zone}."

# ------------------------------------------------------------------
# Chatbot Q&A Functions
# ------------------------------------------------------------------
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["Hello there", "Hey!", "Hi!", "Greetings!", "Welcome!"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def generate_response(user_response):
    global sent_tokens
    # Check if the query mentions a zone
    zone_match = re.search(r'zone\s*([\d\.]+)', user_response, re.IGNORECASE)
    if zone_match:
        zone_str = zone_match.group(1)
        return extract_zone_sentences(zone_str, sent_tokens)
    
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        return "I'm sorry, I didn't catch that."
    else:
        return sent_tokens[idx]

# ------------------------------------------------------------------
# Tweet Validation Functions (unchanged)
# ------------------------------------------------------------------
LEDGER_RPC = "https://17dc-2601-646-102-3580-3011-baf3-e78-28b.ngrok-free.app"
SUBMIT_URL  = f"{LEDGER_RPC}/submit"

try:
    sensors = pd.read_csv("final_sensors_zones.csv")
    sensors["timestamp"] = pd.to_datetime(sensors["timestamp"])
except Exception as e:
    st.error("Error loading sensor data: " + str(e))
    sensors = pd.DataFrame()

HAZARD_PATTERNS = {
    "fire":       r"\bfire\b",
    "earthquake": r"\bearthquake\b|\bquake\b",
    "flood":      r"\bflood\b",
    "evacuate":   r"\bevacuate\b|\bevacuation\b|\bemergency\b"
}

def extract_hazard(text):
    for hazard, pattern in HAZARD_PATTERNS.items():
        if re.search(pattern, str(text), flags=re.I):
            return hazard
    return "unknown"

def map_hazard_to_sensors(hazard):
    mapping = {
        "flood":      ["flood", "humidity"],
        "fire":       ["temp", "humidity"],
        "earthquake": ["seismic"],
        "evacuate":   ["flood", "temp", "seismic", "humidity"],
    }
    return mapping.get(hazard, [])

VALID_THRESHOLD = 60
TIME_WINDOW = "20min"
MIN_ACTIVE = 1
HIGH_PCT_REQ = 20
MEAN_REQ = 20

def validate_tweet(row):
    if row["tweet_hazard"] == "unknown":
        return "ignore", 0, 0, 0

    zone = row["zone_id"]
    hazard = row["tweet_hazard"]
    tweet_time = row["timestamp"]

    window = sensors[
        (sensors["zone_id"] == zone) &
        (sensors["sensor_type"].isin(map_hazard_to_sensors(hazard))) &
        (abs(sensors["timestamp"] - tweet_time) <= pd.Timedelta(TIME_WINDOW))
    ]
    
    if window.empty:
        return "fake", 0, 0, 0

    mean_read = window["reading_value"].mean()
    pct_high = (window["reading_value"] >= VALID_THRESHOLD).mean() * 100
    n_active = (window["status"].str.lower() == "active").sum()

    if pct_high >= HIGH_PCT_REQ and mean_read >= MEAN_REQ and n_active >= MIN_ACTIVE:
        verdict = "valid"
    elif pct_high < 5:
        verdict = "fake"
    else:
        verdict = "uncertain"
    return verdict, pct_high, mean_read, n_active

def push_tweet(payload):
    response = requests.post(SUBMIT_URL, json=payload, timeout=10, verify=False)
    return response.status_code

def process_chatbot_tweet(tweet_text, zone_id, ts_str):
    try:
        tweet_timestamp = pd.to_datetime(ts_str)
    except Exception as e:
        return f"Invalid timestamp format: {e}"

    tweet_hazard = extract_hazard(tweet_text)
    tweet_dict = {
        "text": tweet_text,
        "zone_id": zone_id,
        "timestamp": tweet_timestamp,
        "tweet_hazard": tweet_hazard
    }
    verdict, pct_high, mean_read, n_active = validate_tweet(tweet_dict)

    payload = {
        "tweet_id": "manual-" + dt.datetime.now().strftime("%Y%m%d%H%M%S"),
        "zone_id": zone_id,
        "hazard": tweet_hazard,
        "status": verdict,
        "timestamp": tweet_timestamp.isoformat(),
        "pct_high": pct_high,
        "mean_read": mean_read,
        "n_active": n_active
    }
    push_result = push_tweet(payload)
    if push_result == 200:
        return (f"Tweet validated as '{verdict}'. Mean sensor reading: {mean_read:.2f}, "
                f"percent high: {pct_high:.1f}%, active sensors: {n_active}. "
                f"Successfully pushed to blockchain.")
    else:
        return f"Error sending tweet to the ledger. Status code: {push_result}"

# ------------------------------------------------------------------
# Sidebar Navigation
# ------------------------------------------------------------------
mode = st.sidebar.radio("Navigation", ["Chat", "Validate Tweet", "About"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------------------------------------------------
# Chat Mode
# ------------------------------------------------------------------
if mode == "Chat":
    st.title("NeuroPolis Chatbot")
    st.markdown("Your digital nerve center for crisis intel—integrated Q&A and tweet validation at your fingertips!")
    st.subheader("General Chat")
    
    # Create a fixed chat container using an st.empty() placeholder.
    chat_placeholder = st.empty()
    def update_chat():
        chat_html = '<div class="chat-container">'
        for sender, message in st.session_state.chat_history:
            if sender == "You":
                chat_html += f'<div class="chat-message user"><strong>You:</strong> {message}</div>'
            else:
                chat_html += f'<div class="chat-message bot"><strong>Freestyle Genie:</strong> {message}</div>'
        chat_html += '</div>'
        chat_placeholder.markdown(chat_html, unsafe_allow_html=True)
    
    update_chat()
    
    # Fixed input area at bottom
    user_input = st.text_input("Type your message here...", key="chat_input")
    if st.button("Send", key="chat_send") and user_input:
        greet = greeting(user_input)
        if greet:
            bot_response = greet
        else:
            bot_response = generate_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Freestyle Genie", bot_response))
        update_chat()

# ------------------------------------------------------------------
# Tweet Validation Mode
# ------------------------------------------------------------------
elif mode == "Validate Tweet":
    st.title("NeuroPolis Chatbot – Tweet Validation")
    st.markdown("Validate tweets against sensor data and push the outcome to the blockchain.")
    tweet_text = st.text_area("Enter tweet text:", key="tweet_text_area")
    zone_id = st.text_input("Enter zone (e.g., ZoneA):")
    ts_str = st.text_input("Enter tweet timestamp (YYYY-MM-DD HH:MM:SS):")
    if st.button("Validate Tweet"):
        if tweet_text and zone_id and ts_str:
            result = process_chatbot_tweet(tweet_text, zone_id, ts_str)
            st.markdown(f"<p><strong>Freestyle Genie:</strong> {result}</p>", unsafe_allow_html=True)
        else:
            st.error("Please fill in all the tweet details.")

# ------------------------------------------------------------------
# About Page
# ------------------------------------------------------------------
elif mode == "About":
    st.title("NeuroPolis: From Signal to Strategy")
    st.markdown(
    """
    **NeuroPolis is a next-generation AI-powered Crisis Intelligence System**  
    designed to act as the digital nerve center of a smart city during crises. 
    It transforms fragmented, multi-source urban data into a unified intelligence framework 
    that enables real-time detection, forecasting, coordination, and verifiable data integrity 
    using blockchain technology—ensuring predictability, transparency, and trust.
    
    ---
    **What Does the Chatbot Do?**  
    - **Document Q&A:** Answers general questions about the system's mission and underlying data.  
    - **Zone-based Response:** Scans the corpus for sentences related to a specific zone and returns all matched content.  
    - **Tweet Validation:** Validates tweets in real time against sensor data and stores results on the blockchain.
    
    NeuroPolis is not just a model—it’s a mission-critical intelligence layer that cities can trust when lives are on the line.
    """,
    unsafe_allow_html=True)
    
st.markdown("<br><br><div style='text-align: center;'>NeuroPolis | Built for Hackathon by Data Framers | Aggie Hacks 25</div>",
            unsafe_allow_html=True)
