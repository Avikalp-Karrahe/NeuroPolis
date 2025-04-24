
# 🌆 NeuroPolis: The Brain of a Smart City During Crisis
🥉 **3rd Place Winner** + 🧬 **Best Mixed Team Award – Aggie Hackathon 2025**

> By: Avikalp Karrahe, Rachel Guo, Adeyemi Olalemi, Chaitanya (CK) Khot  
> Tools: Python · Streamlit · XGBoost · GPT-4 · GeoPandas · [StructuredLabs/preswald](https://github.com/StructuredLabs/preswald) · **Full** Blockchain backbone

---

## 🧠 Executive Summary

**NeuroPolis** is an AI-powered crisis-intelligence command centre that helps smart-city leaders detect threats, predict cascading failures, and act decisively—even when power, comms, and public trust are fading. It fuses live sensors, social media, and infrastructure data into a single, explainable source of truth.

---

## 🌀 Hurricane Ian Case Study  
*Florida, September 2022*

| Result | Impact |
| ------ | ------ |
| **3-stage cascade predicted** (flood → hospital strain → power outage) **4 h before ground truth** | Allowed cities to stage generators & ambulance surge crews |
| **7 fake-tweet clusters flagged** within 3 km of landfall | Prevented misinformation-driven traffic jams on evacuation routes |
| **2.3 h faster** end-to-end response vs historical timeline | Demonstrated life-saving potential in a live replay environment |

---

## 🛠️ System Architecture & Innovation

### How it Works (Signal ➜ Strategy)
1. **Ingestion Layer** – websockets & batch jobs pull sensors, tweets, power logs, and hospital feeds every 60 s  
2. **Fusion & Validation** – geospatial join + outlier repair + blockchain hash for raw packets  
3. **Intelligence Engines**:  
   - Cascade Disaster Predictor (zone-aware models forecast multi-hop failures)  
   - Hospital Overload Estimator  
   - Misinformation Detector (sensor-grounded contradiction logic)  
4. **Decision Engine** – GPT-4 ranks response tactics by cost, reach, and time-to-implement  
5. **Delivery Layer** – Streamlit dashboard, REST API, chatbot

---

## 🧠 About the Chatbot

The NeuroPolis Chatbot enables operators to ask:
- “What’s happening in Zone C right now?”
- “Is this tweet real?”
- “Recommend actions if risk ≥ 0.75 in Zone B.”

<p align="center">
  <img alt="Chatbot Overview" src="Demo/About%20me.png" width="80%"/>
</p>

---

## 🎥 Demonstration

### 🔹 General Chatbot Interface
<video src="Demo/Chatbot.mp4" controls width="100%"></video>

### 🔹 Tweet Misinformation Detection
<video src="Demo/Tweet%20Validation.mp4" controls width="100%"></video>

### 🔹 Blockchain Trust Ledger Demo
<video src="Demo/Trust_Ledger_prototype.mp4" controls width="100%"></video>

---

## 📄 Documentation
📊 [Final Deck (PDF)](Docs/Data%20Farmers%20-%20Neuropolis%20AggieHacks25.pdf)

---

## 👥 Team
- Avikalp Karrahe  
- Rachel Guo  
- Adeyemi Olalemi  
- Chaitanya (CK) Khot  

---

## 📜 License
MIT License – Open-source for research and public good.
