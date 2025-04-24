
# 🌆 NeuroPolis: The Brain of a Smart City During Crisis
🥉 3rd Place Winner + 🧬 Best Mixed Team Award – Aggie Hackathon 2025

**Team:** Avikalp Karrahe, Rachel Guo, Adeyemi Olalemi, Chaitanya (CK) Khot  
**Tools:** Python · Streamlit · XGBoost · GPT-4 · GeoPandas · Blockchain · StructuredLabs/preswald

---

## 🧠 Executive Summary

As cities face increasingly complex disasters—floods, power failures, misinformation spikes—decision-makers are left paralyzed without trusted, real-time intelligence.

**NeuroPolis** is an AI-powered crisis intelligence system that predicts cascading failures, flags fake tweets, and recommends explainable emergency actions—all from a unified interface. Built for first responders, city ops teams, and emergency managers, it’s the digital brain of a smart city under stress.

---

## 🚨 Business Problem

When sensors scream, dashboards crash, and misinformation spreads, city leaders ask:

- What’s happening and where?
- Is social media spreading false alerts?
- Which zones are at highest risk?
- What actions must we take now?

**NeuroPolis** bridges siloed systems and filters noise—delivering real-time strategy, not just data.

---

## 📊 Data & Methodology

**Data Sources:**

- 50,000+ rows across flood, seismic, hospital, power, social media, GeoJSON maps, and economic indicators

**Preprocessing:**

- Time alignment & outlier correction for sensors
- Spatial aggregation with buffers (via GeoPandas)
- Fusion of text (tweets) + geo + time series for modeling

**Models:**

- Cascading Disaster Predictor: Random Forest + zone-aware rules
- Hospital Overload Estimator: risk classification engine
- Fake Tweet Detector: contradiction engine (sensor-grounded)
- GPT-4 Action Generator: scenario-specific recommendations
- Blockchain Validator: Hyperledger-based alert timestamping

---

## 🌀 Hurricane Ian Case Study

Simulated Hurricane Ian (Florida, 2022) to test NeuroPolis against a real disaster timeline.

**Impact:**
- Predicted a 3-stage cascade: flooding → hospital strain → power outage
- Detected 7 fake tweets within 3km of the affected zone
- Suggested early evacuation + reroute alerts
- Accelerated decision-making by 2.3 hours

---

## 🎥 Demonstration

📺 [Chatbot Interface Demo](Demo/Chatbot.mp4)  
🛡️ [Tweet Validation Demo](Demo/Tweet%20Validation.mp4)  
🔗 [Blockchain Ledger Demo](Demo/Trust_Ledger_prototype.mp4)

---

## 📄 Presentation & Code

📂 [Download Final Deck (PDF)](Docs/Data%20Farmers%20-%20Neuropolis%20AggieHacks25.pdf)  
📁 [Explore Project Files & Codebase](../../tree/main)

---

## 📈 Key Insights

1. **Cascading Disaster Prediction**
   - 83% recall for multi-stage events
   - Real-time zone alerts with severity mapping

2. **Fake News Filtering**
   - 91% precision using contradiction logic
   - Blockchain-based tamper-proof alert logs

3. **AI-Driven Action Planning**
   - GPT-4 tailored emergency actions
   - Reduced decision latency by over 80%

---

## 👥 Team

- Avikalp Karrahe  
- Rachel Guo  
- Adeyemi Olalemi  
- Chaitanya (CK) Khot

---

## 📜 License

MIT License – Open source for research and public good.
