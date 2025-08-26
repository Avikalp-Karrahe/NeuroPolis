<p align="center">
  <a href="#contributors-"><img alt="Contributors" src="https://img.shields.io/badge/Contributors-4-371C58?style=flat-square&logo=github&logoColor=white"/></a>
  <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/License-MIT-007ACC?style=flat-square&logo=mit&logoColor=white"/></a>
  <a href="#"><img alt="Aggie Hacks 25 Finalist" src="https://img.shields.io/badge/Aggie_Hacks_25–Finalist-EE6352?style=flat-square"/></a>
  <a href="#"><img alt="Bronze Beacon Award" src="https://img.shields.io/badge/Bronze_Beacon_Award-CD7F32?style=flat-square&logo=award&logoColor=white"/></a>
  <a href="#"><img alt="Best Mixed Team Award" src="https://img.shields.io/badge/Best_Mixed_Team_Award-512DA8?style=flat-square&logo=award&logoColor=white"/></a>
</p>

# 🌆 NeuroPolis: The Brain of a Smart City During Crisis

<p align="center">
  <img src="https://github.com/Avikalp-Karrahe/NeuroPolis/blob/main/Docs/Cover_image.png" alt="NeuroPolis Cover" width="700"/>
</p>

**Turning complex urban signals into clear, actionable strategies—in seconds.**

> **TL;DR:** Real-time AI predicts disasters, verifies information, visualizes risks, and recommends life-saving actions.

---

## 🏆 Awards
- 🥉 **Bronze Beacon Award** – Aggie Hackathon 2025  
- 🧬 **Best Mixed Team Award** – Aggie Hackathon 2025  

---

## 👥 Team Members
- [Avikalp (Avi) Karrahe](https://github.com/Avikalp-Karrahe)  
- Rachel Guo  
- [Chaitanya (CK) Khot](https://github.com/ckkhot)  
- Adeyemi Olalemi  

---

## 📋 Table of Contents
1. [Executive Summary](#executive-summary)  
2. [The Challenge](#the-challenge)  
3. [How It Works](#how-neuropolis-works-from-signals-to-strategy)  
4. [Innovation Highlights](#innovation-highlights)  
5. [Case Study: Hurricane Ian](#case-study-hurricane-ian)  
6. [Data & Methodology](#data--methodology)  
7. [Live Demo Previews](#live-demo-previews)  
8. [Key Insights](#key-insights)  
9. [Installation & Quick Start](#installation--quick-start)  
10. [Contributing](#contributing)  
11. [License & Acknowledgments](#license--acknowledgments)  
12. [Contributors](#contributors-)

---

## 🧠 Executive Summary
NeuroPolis is an AI-powered crisis intelligence platform that empowers cities to **anticipate**, **visualize**, and **respond** to cascading disasters in real time. By fusing diverse data sources—from flood sensors to social media chatter—NeuroPolis delivers unified intelligence and clear action plans within seconds.

Our platform clinched the Bronze Beacon Award and Best Mixed Team Award at Aggie Hackathon 2025 for its robust execution, cross-functional innovation, and high-impact potential.

---

## 🚩 The Challenge
Smart cities face **compound crises**: floods trigger power outages, hospitals are overwhelmed, and misinformation spreads panic. Decision-makers struggle with siloed data and delayed insights, hindering effective, coordinated responses.

NeuroPolis solves this by acting as the city’s **digital brain**, unifying real-time signals into **proactive strategies**.

---

## 🔄 How NeuroPolis Works: From Signals to Strategy
1. **Cascading Disaster Prediction**  
   - **Data Fusion:** Real-time sensor readings, weather APIs, and historical disaster patterns.  
   - **Ensemble Models:** Random Forest, XGBoost, LightGBM—to forecast chain events like flood → outage → hospital overload.  
   - **Feature Weights:** Wind (27%), rainfall (26%), severity index (33%), casualties (8%).

2. **Misinformation Detection**  
   - **Internal Validation:** Cross-check social posts vs. sensor data within ± 10 min (≥ 70% sensor agreement for “Severity Support”).  
   - **External Consensus:** Blockchain-based Trust Ledger (HyperLedger Fabric) ensures every flag is immutable and auditable.

3. **Live Risk Visualization**  
   - **Dynamic Maps:** Interactive geospatial dashboards with severity scores (1–10).  
   - **UI Alerts:** Color-coded zones—green to red—indicate safety levels.

4. **Decision Recommendation Engine**  
   - **AI-Generated Plans:** GPT-4 synthesizes clear steps (e.g., “Evacuate Zone C if flood > 75%”).

5. **AI Chatbot Interface**  
   - **Conversational Queries:** Ask questions and get immediate, data-driven action steps—no manual data digging required.

---

## 💡 Innovation Highlights
- **Intel Engine (Internal ML):** Real-time forecasting, risk classification, and anomaly detection—powered by robust ensembles.  
- **Trust Ledger (Blockchain):** Immutable audit trails for every critical alert and misinformation event.

These dual layers guarantee **accuracy**, **accountability**, and **trust**—making NeuroPolis uniquely reliable for life-critical decisions.

---

## 🌀 Case Study: Hurricane Ian
In a **Hurricane Ian** simulation (Florida, 2022), NeuroPolis achieved:
- **70% fatality reduction** via early evacuation alerts.  
- **$11 billion** saved through proactive infrastructure mapping.  
- **60% boost** in emergency asset efficiency.  
- **~91 lives saved** by optimizing hospital rerouting and triage.

---

## 📊 Data & Methodology
**Sources (50 k+ records):** Flood/seismic/weather sensors, hospital & power logs, social media streams, energy stats, GeoJSON maps.

**Workflow:**
1. Isolation Forest outlier detection  
2. Temporal (± 10 min) & geospatial zoning (GeoPandas)  
3. Ensemble forecasting (RF, XGB, LGBM)—92% accuracy for overload predictions  
4. BERT NLP with spatiotemporal filters for fake‐tweet detection  
5. GPT-4 real-time plan synthesis

---

## 🚀 Live Demo & Visual Samples

| Feature               | Preview / Link                                |
|-----------------------|-----------------------------------------------|
| 🤖 **Chatbot**        | ![Chatbot](Demo/About%20me.png)  [▶️](Demo/Chatbot.mp4) |
| 🐦 **Tweet Validation** | ![Tweet](Demo/Tweet%20Validation.png)  [▶️](Demo/Tweet%20Validation.mp4) |
| 🔗 **Trust Ledger**   | ![Ledger](Demo/Trust%20Ledger.png)  [▶️](Demo/Trust_Ledger_prototype.mp4) |
| 🌡️ **Sensor Status**   | ![Status](Demo/Sensor%20status.jpeg)           |
| 📊 **Risk Dashboard** | ![Dashboard](Demo/risk%20dashboard.png)         |

---

## 🔑 Key Insights
1. **Proactive Management:** Stage evacuations hours ahead.  
2. **Misinformation Containment:** > 90% fake‐tweet accuracy.  
3. **Efficiency Gains:** Decision latency down > 99%; asset utilization up 60%.

---

## ⚙️ Installation & Quick Start
```bash
# Clone repository
git clone https://github.com/Avikalp-Karrahe/NeuroPolis.git
cd NeuroPolis

# Setup environment
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run App/main.py
```

Open <http://localhost:8501> to interact.

---

## 🤝 Contributing

**Ready to make an impact on crisis intelligence and advance your data science career?**

NeuroPolis offers **5 strategic contribution categories** designed for senior data scientists and ML engineers:

🧠 **Advanced ML & AI** - Multi-modal disaster prediction, ensemble optimization, NLP for crisis communication  
📊 **Data Engineering & MLOps** - Streaming pipelines, model deployment, scalable infrastructure  
🔗 **Blockchain & Trust Systems** - Smart contracts, decentralized AI governance, privacy-preserving verification  
🎨 **Advanced Visualization & UX** - 3D city visualization, explainable AI interfaces, geospatial analytics  
🔬 **Research & Innovation** - Novel algorithms, ethical AI, academic contributions  

### Portfolio Benefits
- **Technical Depth**: Demonstrate expertise in production ML systems and real-time analytics
- **Industry Relevance**: Smart city and disaster management is a $124B+ market with massive social impact
- **Career Advancement**: Showcase skills in MLOps, distributed systems, and AI ethics that top-tier companies value
- **Recognition**: Gold/Silver/Bronze contributor recognition with co-authorship opportunities

### Quick Start
```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/NeuroPolis.git
cd NeuroPolis

# Set up development environment
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Start contributing
git checkout -b feature/your-amazing-contribution
```

📋 **See our comprehensive [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines, development setup, and contribution opportunities.**

---

## 📜 License & Acknowledgments
- Distributed under the [MIT License](LICENSE).  
- Thanks to Aggie Hackathon organizers, mentors, and open-source projects.

---

## 🎉 Contributors
<a href="https://github.com/Avikalp-Karrahe/NeuroPolis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Avikalp-Karrahe/NeuroPolis" alt="Contributors"/>
</a>

**A big applause to our team:** Avikalp Karrahe, Rachel Guo, Chaitanya Khot, Adeyemi Olalemi.
