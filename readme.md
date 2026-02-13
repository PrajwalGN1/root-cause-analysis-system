#  Root Cause Analysis System (Real-Time System Monitoring)

##  Overview

This project is a real-time **Root Cause Analysis (RCA) system** that:

- Collects real system metrics (CPU, Memory, Disk, Network)
- Detects abnormal behavior using unsupervised machine learning
- Identifies the root cause based on time-based analysis
- Provides human-readable explanations
- Visualizes results using an interactive Streamlit dashboard

Unlike simple anomaly detection projects, this system goes one step further by identifying **which resource failed first**, helping diagnose the actual root cause.

---

#  Problem Statement

Modern applications fail due to:

- CPU overload  
- Memory leaks  
- Disk saturation  
- Network congestion  

Monitoring tools often show that “something is wrong,” but they do not answer:

- What exactly caused the failure?  
- When did it start?  
- Which component triggered the issue?  

This project solves that problem using **temporal anomaly detection and causal reasoning**.

---

#  Project Architecture

System Metrics (CPU, Memory, Disk)  
        ↓  
Data Collection (psutil)  
        ↓  
Anomaly Detection (Isolation Forest)  
        ↓  
Temporal Root Cause Analysis  
        ↓  
Explanation Engine  
        ↓  
Streamlit Dashboard  

---

#  How It Works

## 1️⃣ Real-Time Data Collection

The system collects:

- CPU usage  
- Memory usage  
- Disk usage  
- Network activity  

These metrics are gathered directly from the operating system using `psutil`.

Why real metrics?

- No simulated data  
- No artificial noise  
- Real-world behavior  

---

## 2️⃣ Unsupervised Anomaly Detection

We use **Isolation Forest**, an unsupervised ML algorithm, to detect abnormal patterns.

Why unsupervised?

- Real systems do not have labeled failures  
- Failures are rare and unpredictable  
- The system learns normal behavior automatically  

---

## 3️⃣ Root Cause Identification

The key idea:

The first resource that becomes abnormal is likely the root cause.

Example:

Time T1 → CPU spikes  
Time T2 → Memory rises  
Time T3 → Disk affected  

Root Cause → CPU saturation  
Memory and Disk issues are downstream effects.

---

## 4️⃣ Explanation Layer

The system converts raw numbers into human-readable output:

First anomaly detected at 12:45:21  
CPU value: 92%  
Root cause: CPU saturation  

This improves interpretability and trust.

---

## 5️⃣ Visualization Dashboard

The Streamlit dashboard provides:

- Resource usage graphs  
- Anomaly highlights  
- Tabular anomaly reports  
- Root cause summary  

This allows visual validation of system failures.

---

# 📂 Project Structure

root-cause-analysis/  

├── collector/          → Metric collection  
├── rca/                → Anomaly detection & RCA logic  
├── dashboard/          → Streamlit UI  
├── data/               → Generated CSV files  
├── requirements.txt  
└── README.md  

---

# ▶️ How to Run

1. Install dependencies

pip install -r requirements.txt

2. Collect system metrics

python collector/collect_metrics.py

3. Run anomaly detection

python rca/anomaly_detection.py

4. Identify root cause

python rca/root_cause.py

5. Launch dashboard

streamlit run dashboard/app.py

---

#  Real-World Applications

This system can be extended to monitor:

- Web servers  
- Microservices  
- Databases  
- Payment systems  
- Cloud infrastructure  
- Kubernetes clusters  

---

#  Real-Life Advantages

##  Faster Incident Resolution

Reduces Mean Time To Repair (MTTR) by automatically identifying the first failing component.

---

##  Prevents Blind Debugging

Instead of checking everything manually, engineers get a prioritized root cause.

---

##  Works Without Labeled Data

No need for manually tagged failure examples.

---

##  Scalable to Enterprise Systems

The same logic can be applied to:

- API services  
- Payment microservices  
- Databases  
- Cloud monitoring systems  

---

##  Explainable AI

Not a black box.

Provides:

- Timestamp  
- Metric values  
- Root cause reasoning  

---

##  Demonstrates Engineering Skills

This project showcases:

- Time-series analysis  
- Unsupervised machine learning  
- System design thinking  
- Causal reasoning  
- End-to-end pipeline building  

---

#  Key Concepts Demonstrated

- Time-based anomaly detection  
- Causal inference logic  
- System observability  
- Unsupervised machine learning  
- Real-time monitoring  
- Explainable AI  

---

#  Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Psutil  
- Streamlit  
- Matplotlib  

---

#  Future Improvements

- Service-level metrics (API, Database, Payment)  
- Log analysis using NLP  
- Confidence scoring  
- Real-time streaming monitoring  
- Cloud deployment  
- Alerting system integration  

---

#  Conclusion

This project demonstrates how to move beyond anomaly detection and perform true root cause analysis using real system metrics and temporal reasoning.

It bridges the gap between machine learning and real-world system monitoring.



