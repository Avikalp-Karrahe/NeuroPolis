
# 🌆 NeuroPolis: The Brain of a Smart City During Crisis  
🥉 3rd Place Winner + 🧬 Best Mixed Team Award – Aggie Hackathon 2025

🔗 [📄 View Final Presentation Deck (PDF)](https://github.com/Avikalp-Karrahe/NeuroPolis/blob/main/Docs/Data%20Farmers%20-%20Neuropolis%20AggieHacks25.pdf)  
🔗 [🧠 Read Executive Summary](https://github.com/Avikalp-Karrahe/NeuroPolis/blob/main/Docs/NeuroPolis%20-%20Executive%20Summary.pdf)

---

## 🧠 Executive Summary

As natural disasters become more frequent and social misinformation spreads faster than emergency response systems can react, cities are left vulnerable.

**NeuroPolis** is a real-time, AI-powered disaster intelligence dashboard designed to predict disasters, flag fake social media posts, and generate actionable emergency plans — all within seconds.

This project was awarded **3rd Prize and Best Mixed Team** at the 2025 Aggie Hackathon for innovation, intelligence modeling and impact potential.

---

## 🚨 Business Problem

In crisis situations like floods or cyberattacks, city leaders face overwhelming volumes of noisy data and misinformation.  
Key questions we address:

- What type of disaster is unfolding right now, and where?  
- Is social media reporting false information?  
- How severe are the consequences?  
- What immediate actions should the city take?

---

## 📊 Data & Methodology

**Dataset:**  
50,000+ rows across sensors, weather, social media, infrastructure maps

**Preprocessing:**  
- Outlier detection in weather via Isolation Forest  
- Sensor classification via rule-based logic  
- Location matching using geopy and GeoJSON infrastructure maps  
- Data fusion of time-series, spatial, and text features

**Models:**  
- **Disaster Severity Prediction:** Rule-based logic + weather-based mapping  
- **Hospital Overload Risk:** Random Forest Classifier trained on severity, disaster type and hospital proximity (92% accuracy)  
- **Fake Tweet Detection:** Proximity validation + BERT-based NLP  
- **Emergency Plan Generation:** GPT-4 generated concise, scenario-based action prompts

---

## 🛠️ Innovation Highlights

- 🔗 **Blockchain-Backed Alert Validation**  
  Verifiable alerts and misinformation logs recorded in a tamper-proof ledger using Hyperledger Fabric.

- 🧠 **GPT-4 Strategic Action Engine**  
  Custom emergency actions generated in under 3 seconds—tailored to the risk zone and severity.

- 🌐 **Multimodal Fusion & Sensor Contradiction**  
  Cross-verifies social chatter against physical sensor readings using contradiction logic with 91% precision.

- 🧪 **Zone-Aware Forecasting**  
  Geo-temporal prediction models that recognize and simulate cascading failures (e.g., flood → power outage → hospital overload).

---

## 🧩 How NeuroPolis Works

1. **Data Ingestion**  
   Pulls real-time flood, seismic, hospital, weather, and social media feeds every 60 seconds.

2. **Fusion & Cleaning**  
   Applies timestamp alignment, sensor repair, and spatial joins across infrastructure layers.

3. **Intelligence Layer**  
   - Disaster Chain Predictor (Random Forest + Rule Chains)  
   - Overload Estimator (zone-based classifier)  
   - Misinformation Detector (sensor contradiction logic)  
   - GPT-4 Planner (context-aware action ranking)

4. **Decision Delivery**  
   Broadcasts actions to Streamlit dashboard, chatbot interface, and operator API.

---

## 🎥 Demonstration

- [🧠 Chatbot Interface](Demo/Chatbot.mp4)  
- [🛡️ Tweet Misinformation Detection](Demo/Tweet%20Validation.mp4)  
- [🔗 Blockchain Trust Ledger Demo](Demo/Trust_Ledger_prototype.mp4)

---

## 📈 Key Impact Insights

- **Cascading Disaster Prediction**  
  → Predicted 3-stage chain 4 hours before impact (flood → hospital → outage)

- **Fake News Filtering**  
  → 91% precision in detecting misinformation near disaster zones

- **GPT-4 Planning**  
  → Reduced human decision-making time by over 80%

---

## 👥 Team

- Avikalp Karrahe  
- Rachel Guo  
- Adeyemi Olalemi  
- Chaitanya (CK) Khot

---

## 📜 [MIT License – Open source for research and public good](LICENSE)  
Feel free to use, remix, and build upon this project. Attribution appreciated.
