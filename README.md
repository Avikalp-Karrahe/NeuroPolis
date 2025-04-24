# 🌆 NeuroPolis: The Brain of a Smart City During Crisis  
🥉 Bronze Beacon Award + 🧬 Best Mixed Team Award – Aggie Hackathon 2025

**Code:** [NeuroPolis Python Code](https://github.com/Avikalp-Karrahe/NeuroPolis)  
**Report:** [NeuroPolis Executive Summary](https://github.com/Avikalp-Karrahe/NeuroPolis/blob/main/Docs/NeuroPolis%20-%20Executive%20Summary.pdf)  
**Team:** Avikalp (Avi) Karrahe, Rachel Guo, Chaitanya (CK) Khot, Adeyemi Olalemi  
**Tools:** Python, Streamlit, Random Forest, XGBoost, LightGBM, OpenAI GPT-4, GeoPandas, Hyperledger Fabric

---

## 🧠 Executive Summary

As natural disasters grow more frequent and social misinformation spreads faster than emergency response systems can react, cities face escalating risks. NeuroPolis is an AI-powered crisis intelligence platform that transforms fragmented urban data—sensors, social media, hospital logs, energy usage, and infrastructure maps—into predictive insights, real-time risk visualizations, and actionable emergency plans in seconds.

This system earned the Bronze Beacon Award and Best Mixed Team Award at the 2025 Aggie Hackathon for strong execution, cross-functional collaboration, and impact potential.

---

## 🚩 The Challenge

Urban crises cascade: a flood triggers power outages, hospitals become overwhelmed, and misinformation fuels panic online. Emergency teams are inundated with siloed data streams and lack a unified decision system to anticipate what comes next and coordinate rapid, trusted responses.

---

## 💡 Our Solution

NeuroPolis serves as the city’s digital brain during multi-disaster scenarios, offering:

- **Cascading Disaster Prediction:** Learns from historical patterns and real-time signals to forecast linked events (e.g., flood → power outage → hospital overload).
- **Misinformation Detection:** Flags fake posts by cross-verifying social media chatter against ground-truth sensor data and official records.
- **Live Risk Visualization:** Renders interactive zone maps that update risk levels continuously.
- **Decision Recommendation Engine:** Generates concise, scenario-based action plans via GPT-4, ensuring leaders can act decisively.

---

## 📊 Data & Methodology

**Data Sources**  
50,000+ records from flood, seismic, and weather sensors; hospital capacity and power logs; normalized energy usage; social media streams (real + synthetic); and GeoJSON infrastructure maps.

**Preprocessing & Modeling**  
- Outlier detection using Isolation Forest for weather anomalies  
- Rule-based sensor classification and temporal alignment (±10 min)  
- Geospatial zone matching with GeoPandas  
- Ensemble learning (Random Forest, XGBoost, LightGBM) forecasting disaster severity and hospital overload risk (92% accuracy)  
- BERT-based NLP and proximity rules (>3 km, >1 hr) for fake tweet detection  
- GPT-4 integration for real-time emergency plan generation

---

## 🚀 Demonstration Highlights

- **Predictive Forecasting:** Input a future timestamp to view predicted severity scores, hospital risk levels, and AI-generated action plans.  
- **Misinformation Flagging:** Detect and label suspicious tweets by comparing against sensor evidence within defined spatiotemporal windows.  
- **Historical Pattern Analysis:** Aggregate and visualize past events to uncover trends and optimize resource allocation.

---

## 🔑 Key Insights

1. **Proactive Crisis Management**  
   Early warnings up to hours ahead enable proactive evacuations and staged resource deployment.

2. **Trustworthy Information**  
   >90% accuracy in fake tweet detection reduces panic and prevents costly false alarms.

3. **Optimized Response**  
   AI-generated emergency plans cut decision-making lag by >99%, boosting emergency asset efficiency by 60%.

---

## 👥 Team & Acknowledgments

- **Avikalp (Avi) Karrahe** (MSBA, Project Manager & Data Scientist)  
- **Rachel Guo** (MSBA, Data Engineer)  
- **Chaitanya (CK) Khot** (MBA, ML Engineer)  
- **Adeyemi Olalemi** (MBA, Frontend Developer)

Thank you to the Aggie Hackathon organizers, mentors, and fellow participants for their support and feedback.

---

## 📜 License

MIT License — Open source for research and public good. Feel free to use, remix, and build on NeuroPolis. Attribution appreciated.
