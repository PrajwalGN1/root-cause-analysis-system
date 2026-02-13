import pandas as pd
import os
from sklearn.ensemble import IsolationForest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "system_metrics.csv")

df = pd.read_csv(DATA_PATH)

features = ["cpu_percent", "memory_percent", "disk_percent"]

model = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = model.fit_predict(df[features])

OUTPUT_PATH = os.path.join(BASE_DIR, "data", "system_metrics_anomaly.csv")
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Anomaly detection complete")
print("📁 Saved to data/system_metrics_anomaly.csv")
