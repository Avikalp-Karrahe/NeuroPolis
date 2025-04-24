# 🌆 NeuroPolis: The Brain of a Smart City During Crisis  
🥉 Bronze Beacon Award + 🧬 Best Mixed Team Award – Aggie Hackathon 2025

**Code:** [NeuroPolis Python Code](https://github.com/Avikalp-Karrahe/NeuroPolis)  
**Report:** [Executive Summary PDF](https://github.com/Avikalp-Karrahe/NeuroPolis/blob/main/Docs/NeuroPolis%20-%20Executive%20Summary.pdf)  
**Team:** Avikalp (Avi) Karrahe, Rachel Guo, Chaitanya (CK) Khot, Adeyemi Olalemi  
**Tools:** Python, Streamlit, Random Forest, XGBoost, LightGBM, BERT, OpenAI GPT-4, GeoPandas, Hyperledger Fabric

---

## 🧠 Executive Summary
As natural disasters grow more frequent and social misinformation spreads faster than emergency response systems can react, cities face escalating risks. NeuroPolis transforms fragmented urban data—sensors, social media feeds, hospital and power logs, energy usage, and infrastructure maps—into predictive insights, real-time visualizations, and actionable emergency plans in seconds.

This platform secured the Bronze Beacon Award and Best Mixed Team Award at the 2025 Aggie Hackathon for strong execution, cross-functional collaboration, and transformative impact.

---

## 🚩 The Challenge
Urban crises cascade: floods trigger power outages, hospitals become overwhelmed, and panic spreads through fake news. Emergency teams drown in siloed data streams and lack a unified system to forecast next steps and coordinate rapid, trusted responses.

---

## 🔄 How NeuroPolis Works: From Signals to Strategy
Imagine it's late at night, our city is under siege—rising floodwaters, cyberattacks disabling power grids, misinformation causing panic, and hospitals nearing capacity. NeuroPolis acts as the city’s intelligent brain, swiftly converting raw signals into clear strategies:

1. **Cascading Disaster Prediction**  
   - We analyze key indicators like high wind speeds (27%), intense rainfall (26%), severity scores (33%), and casualty estimates (8%) to forecast chain reactions—e.g., flood → outage → hospital overload—before they occur.

2. **Misinformation Detection**  
   - **Internal Validation:** Social posts are cross-checked against sensor readings within a 10-minute window and only flagged when ≥70% of sensors corroborate an anomaly ("Severity Support").  
   - **External Consensus:** Critical alerts pass through a blockchain-based Trust Ledger on HyperLedger Fabric, requiring multiple independent confirmations to ensure auditability.

3. **Live Risk Visualization**  
   - Interactive zone maps display real-time Severity Scores (1–10), with anything above 8 triggering immediate alerts—like a traffic light signaling when it’s unsafe to proceed.

4. **Decision Recommendation Engine**  
   - GPT-4 instantly synthesizes all inputs into concise action plans: evacuate if flood >75%, reroute traffic if road access <30%, and redirect ambulances when hospital capacity >90%.

5. **AI Chatbot Interface**  
   - City leaders ask critical questions via chat and receive precise, actionable answers in seconds, without sifting through raw data.

---

## 💡 Innovation Highlights
NeuroPolis’s power comes from two complementary innovations:

- **Intel Engine (Internal ML):**  
  Ensemble models (Random Forest, LightGBM, XGBoost) perform real-time forecasting, risk classification, and anomaly pattern detection—transforming data into proactive insights.

- **Trust Ledger (External Blockchain):**  
  Built on HyperLedger Fabric, this immutable system logs every verified alert and flagged misinformation, providing transparent, timestamped audit trails that reinforce trust in crisis decisions.

Together, these layers ensure intelligence that is both accurate and accountable—turning chaotic data into reliable, auditable action.

---

## 🌀 Hurricane Ian Case Study
In a simulated Hurricane Ian scenario (Florida, 2022), NeuroPolis delivered:

- **70% fatality reduction** through early evacuation recommendations  
- **$11 billion** in economic losses avoided via proactive infrastructure risk mapping  
- **60% boost** in emergency asset efficiency by streamlining resource allocation  
- **~91 lives potentially saved** by accelerating triage and hospital rerouting

These results highlight how NeuroPolis can turn hours of delay into minutes of lead time—and save lives.

---

## 📊 Data & Methodology
**Sources:** 50,000+ records from flood, seismic, weather sensors; hospital and energy logs; social media streams (real + synthetic); GeoJSON infrastructure maps.

**Pipeline:**  
- Outlier detection via Isolation Forest  
- Rule-based sensor classification and ±10 min temporal alignment  
- Geospatial zoning with GeoPandas  
- Ensemble forecasting models (RF, XGB, LGBM) achieving 92% hospital overload accuracy  
- BERT-based NLP with proximity rules (>3 km, >1 hr) for fake tweet detection  
- GPT-4 for real-time plan synthesis

---

## 🚀 Demo Previews
### 🤖 Chatbot Interface
![Chatbot Demo](Demo/About%20me.png)
<video src="Demo/Chatbot.mp4" controls width="480" />

### 🐦 Tweet Validation
<video src="Demo/Tweet%20Validation.mp4" controls width="480" />

### 🔗 Trust Ledger Prototype
<video src="Demo/Trust_Ledger_prototype.mp4" controls width="480" />

---

## 🔑 Key Insights
1. **Proactive Management:** Forecasting up to hours ahead enables staged evacuations and resource deployment.  
2. **Information Integrity:** >90% accuracy in fake tweet detection mitigates panic and prevents false alarms.  
3. **Operational Efficiency:** AI-driven recommendations cut decision lag by >99% and boost asset utilization by 60%.

---

## 👥 Team & Acknowledgments
- Avikalp (Avi) Karrahe (MSBA, Project Manager & Data Scientist)  
- Rachel Guo (MSBA, Data Engineer)  
- Chaitanya (CK) Khot (MBA, ML Engineer)  
- Adeyemi Olalemi (MBA, Frontend Developer)

Thanks to Aggie Hackathon mentors, judges, and fellow teams for feedback and support.

---

## 📜 License
[MIT License](LICENSE) — Open source for research and public good. Attribution appreciated.
