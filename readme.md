#  Root Cause Analysis System (Real-Time Metrics)

An end-to-end Root Cause Analysis (RCA) system that collects real system metrics,
detects anomalies using unsupervised learning, identifies root causes,
and visualizes results via a Streamlit dashboard.

---

##  Features

- Real-time system metric collection (CPU, Memory, Disk, Network)
- Unsupervised anomaly detection (Isolation Forest)
- Root cause identification based on temporal analysis
- Human-readable explanation layer
- Interactive dashboard (Streamlit)

---

##  Project Structure

collector/ → Metric collection  
rca/ → Anomaly detection & root cause logic  
dashboard/ → Streamlit visualization  

---

## ▶ How to Run

1. Install dependencies

2. Collect metrics

3. Run anomaly detection

4. Identify root cause

5. Launch dashboard

---

##  Concept

This system performs time-based anomaly detection on system metrics
and identifies the earliest abnormal signal as the root cause.

---

##  Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib
- Psutil


