# 🌆 NeuroPolis: The Brain of a Smart City During Crisis
🥉 **3rd Place Winner** + 🧬 **Best Mixed Team Award – Aggie Hackathon 2025**

> By: Avikalp Karrahe, Rachel Guo, Adeyemi Olalemi, Chaitanya (CK) Khot  
> Tools: Python, Streamlit, XGBoost, GPT-4, GeoPandas, Blockchain Simulation

---

## 🧠 Executive Summary

**NeuroPolis** is a crisis-time AI command center built to help smart cities detect threats, respond faster, and maintain public trust. It ingests multimodal sensor streams, detects misinformation, simulates cascading disasters, and generates explainable action plans — even during blackouts, misinformation waves, and infrastructure failures.

---

## 🚨 Business Problem

When power grids fail, tweets mislead, and emergency teams go blind — who can think clearly?

**NeuroPolis** addresses:
> ✅ What’s real vs fake?  
> ✅ Where is risk spreading next?  
> ✅ What actions should be taken in seconds?

It bridges siloed departments, grounds social chatter in data, and replaces reaction with anticipation.

---

## 📊 Data & Methodology

**Sources:**  
50,000+ rows across:
- Sensor Readings (flood, humidity, seismic)
- Social Media (real + AI-generated fake posts)
- GeoJSON Infrastructure Maps
- Economic, Weather, Hospital, Power Logs

**Preprocessing Techniques:**
- Zone-aware timestamp alignment  
- Outlier filtering (sensor corruption logic)  
- Location aggregation using geospatial buffers  
- Multimodal fusion: time-series + text + spatial

**Models & Logic Used:**
- 📉 Cascading Disaster Prediction → Random Forest + Rule Chains  
- 🚨 Hospital Overload Estimator → Zone/Severity-based classifier  
- 🧠 Misinformation Detector → Social vs sensor contradiction engine  
- 🔗 Tamper-Proof Ledger → Blockchain-inspired alert validator  
- 💡 GPT-4 for Action Plans → Situation-aware emergency recommendations

---

## 🌀 Hurricane Ian Case Study

We applied NeuroPolis to simulate a real-world disaster: **Hurricane Ian** (Florida, 2022).  
**Key results:**
- Predicted a 3-stage cascade (flooding → hospital strain → power outage)  
- Detected 7 misinformation tweets within 3km of affected zones  
- Suggested early evacuation + reroute alerts based on real sensor drops  
📌 *Insight*: With NeuroPolis live, city response could have been accelerated by 2.3 hours.

---

## 🧠 About the Chatbot

NeuroPolis includes a real-time chatbot interface that allows emergency operators and city leaders to ask:

> “What’s happening in Zone C?”  
> “Is this tweet real?”  
> “What’s your recommended action?”

![Chatbot Overview](About me.png)

---

## 🎥 Demonstration

### 🔹 General Chatbot Interface
<video src="Chatbot.mov" controls width="100%"></video>

### 🔹 Tweet Misinformation Detection
<video src="Tweet Validation.mov" controls width="100%"></video>

### 🔹 Blockchain Trust Ledger Demo
<video src="Trust_Ledger_prototype.mov" controls width="100%"></video>

---

## 📈 Key Takeaways

1. **Disaster Chain Prediction**  
   - Predicted flood → outage → hospital load using geo-temporal patterns  
   - Built real-time decision engine for fast triage

2. **Fake News Flagging**  
   - 91% precision in tweet validation using sensor proximity + contradiction logic  
   - Blockchain-style ledger recorded verified alerts with timestamped hash

3. **Strategic Planning with GPT**  
   - AI-generated actions were accurate, timely, and customized  
   - Reduced human decision time by over 80%

---

## 📄 Documentation

- [📊 Final Presentation Deck (PDF)](Docs/Data Farmers - Neuropolis AggieHacks25.pdf)

---

## 👥 Team

- Avikalp Karrahe  
- Rachel Guo  
- Adeyemi Olalemi  
- Chaitanya (CK) Khot  

---

## 📜 License

This project is open-source and released under the [MIT License](LICENSE).