# 🌆 NeuroPolis: The Brain of a Smart City During Crisis
🥉 **3rd Place Winner** + 🧬 **Best Mixed Team Award – Aggie Hackathon 2025**

> By: Avikalp Karrahe, Rachel Guo, Adeyemi Olalemi, Chaitanya (CK) Khot  
> Tools: Python · Streamlit · XGBoost · GPT‑4 · GeoPandas · [StructuredLabs/preswald](https://github.com/StructuredLabs/preswald) · **Full** Blockchain backbone

---

## 🧠 Executive Summary

**NeuroPolis** is an AI‑powered crisis‑intelligence command centre that helps smart‑city leaders **detect threats, predict cascading failures, and act decisively—even when power, comms, and public trust are fading**. It fuses live sensors, social media, and infrastructure data into a single, explainable source of truth.

---

## 🚨 Business Problem

When flood sensors scream, fake tweets go viral, and dashboards go dark, decision‑makers need seconds—not hours—to understand **what’s real, what’s next, and what to do**.  NeuroPolis answers:

* **What’s real vs fake?**
* **Where is risk spreading next?**
* **Which actions buy the most time and save the most lives?**

---

## 📊 Data & Methodology

| Stream | Size | Purpose |
| ------ | ---- | ------- |
| Environmental sensors (flood, seismic, humidity) | 21 k rows | Ground‑truth for physical risk |
| Social media & news | 12 k posts | Misinformation detection |
| Infrastructure & hospital logs | 9 k rows | Secondary‑effect forecasting |
| GeoJSON maps & economic indicators | 8 k objects | Spatial correlation & resilience scoring |

**Pre‑processing highlights**: zone‑aware timestamp alignment · outlier repair · geospatial buffering · multimodal fusion.

**Model stack**  
`RandomForest ⟶ XGBoost ⟶ RuleChains` for cascade prediction · `GPT‑4` for action plans · custom contradiction logic for misinformation · **Hyperledger Fabric** for tamper‑proof alert history.

---

## 🌀 Hurricane Ian Case Study  
*Florida, September 2022*

> “Can NeuroPolis spot and stop a real disaster chain?”

| Result | Impact |
| ------ | ------ |
| **3‑stage cascade predicted** (flood → hospital strain → power outage) **4 h before ground truth** | Allowed cities to **stage generators & ambulance surge crews** |
| **7 fake‑tweet clusters flagged** within 3 km of landfall | Prevented misinformation‑driven traffic jams on evacuation routes |
| **2.3 h faster** end‑to‑end response vs historical timeline | Demonstrated **life‑saving potential** in a live replay environment |

---

## 🛠️ System Architecture & Innovation

### How it Works (Signal ➜ Strategy)
1. **Ingestion Layer** – websockets & batch jobs pull sensors, tweets, power logs, and hospital feeds every 60 s.  
2. **Fusion & Validation** – geospatial join + outlier repair + blockchain hash for raw packets.  
3. **Intelligence Engines**  
   * *Cascade Disaster Predictor* – zone‑aware temporal models forecast multi‑hop failures.  
   * *Hospital Overload Estimator* – severity‑aware classifier predicts ICU saturation.  
   * *Misinformation Detector* – contradicts social claims with sensor ground truth.  
4. **Decision Recommendation Engine** – GPT‑4 ranks response tactics by cost, reach, and time‑to‑implement.  
5. **Delivery Layer** – Streamlit dashboard, secure REST API, and Chatbot interface broadcast actions to operators.

### Innovation Highlights
* **First open‑source “sensor‑to‑GPT” pipeline** with builtin blockchain audit trail.  
* **Zone‑aware training** handles GPS drift & sensor corruption without manual cleaning.  
* **Contradiction‑logic fake‑news filter** reached **91 % precision** while staying explainable.  
* **Hyperledger Fabric trust ledger** lets agencies verify any alert or tweet decision post‑incident.  
* **Plug‑and‑play modules** → swap models, add cities, or scale to edge devices.

---

## 🧠 About the Chatbot

When seconds count, typing a plain‑English question beats digging through dashboards.  
The **NeuroPolis Chatbot** lets crews ask, for example:

* “What’s happening in Zone C right now?”
* “Is this tweet real?”
* “Recommend actions if risk ≥ 0.75 in Zone B.”

<p align="center">
  <img alt="Chatbot Overview" src="Demo/About%20me.png" width="80%"/>
</p>

---

## 🎥 Demonstration

<table>
<tr><td><b>General Interface</b><br/><video src="Demo/Chatbot.mov" controls width="100%"></video></td></tr>
<tr><td><b>Misinformation Detection</b><br/><video src="Demo/Tweet%20Validation.mov" controls width="100%"></video></td></tr>
<tr><td><b>Blockchain Trust Ledger</b><br/><video src="Demo/Trust_Ledger_prototype.mov" controls width="100%"></video></td></tr>
</table>

*(If the videos do not autoplay on GitHub, open them in the `Demo/` folder.)*

---

## 📈 Key Takeaways

1. **Disaster‑Chain Prediction**  
   • 3‑stage failure chains forecasted with 83 % recall  
   • Real‑time triage engine slashed analysis time from **15 min → 90 s**
2. **Fake‑News Flagging**  
   • **91 % precision** using sensor proximity + contradiction logic  
   • All verified alerts immutably logged on blockchain
3. **Strategic Planning with GPT**  
   • Tailored, step‑by‑step actions generated in < 3 s  
   • **80 % reduction** in human decision latency during tabletop exercise

---

## 📄 Documentation

* **Final Deck (PDF)** – see `Docs/Data Farmers – NeuroPolis AggieHacks25.pdf` for full methodology & results.

---

## 👥 Team

| Name | Role |
| ---- | ---- |
| Avikalp Karrahe | Project Manager · Data Scientist |
| Rachel Guo | ML Engineer |
| Adeyemi Olalemi | Backend & Blockchain Lead |
| Chaitanya (CK) Khot | Front‑end & UX Designer |

---

## 📜 License

Released under the **MIT License** – free for research and non‑commercial use.
