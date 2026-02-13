import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "system_metrics_anomaly.csv")

df = pd.read_csv(DATA_PATH)

print("\n ROOT CAUSE EXPLANATION\n")

thresholds = {
    "cpu_percent": 80,
    "memory_percent": 80,
    "disk_percent": 90
}

first_failure = None
first_time = None

for metric, threshold in thresholds.items():
    failed = df[df[metric] > threshold]
    if not failed.empty:
        t = failed.index.min()
        if first_time is None or t < first_time:
            first_time = t
            first_failure = metric

if first_failure is None:
    print("System is healthy. No significant anomalies detected.")
else:
    row = df.iloc[first_time]
    print(f"First anomaly detected at sample index: {first_time}")
    print(f"Timestamp: {row['timestamp']}")
    print(f"{first_failure.replace('_percent','').upper()} value: {row[first_failure]}%")

    print("\n DATA-DRIVEN ROOT CAUSE:")
    print(f"{first_failure.replace('_percent','').upper()} saturation")
