import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "system_metrics_anomaly.csv")

df = pd.read_csv(DATA_PATH)

thresholds = {
    "cpu_percent": 80,
    "memory_percent": 80,
    "disk_percent": 90
}

anomaly_times = {}

for metric, threshold in thresholds.items():
    anomalous = df[df[metric] > threshold]
    anomaly_times[metric] = anomalous.index.min()

root_cause = min(
    anomaly_times,
    key=lambda k: anomaly_times[k] if pd.notna(anomaly_times[k]) else float("inf")
)

print("🔥 ROOT CAUSE IDENTIFIED")
print(root_cause.replace("_percent", "").upper())
