import psutil
import pandas as pd
from datetime import datetime
import os

SAMPLE_SIZE = 50
INTERVAL = 1

data = []

#  Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#  Ensure data directory exists
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

CSV_PATH = os.path.join(DATA_DIR, "system_metrics.csv")

print(f"Collecting {SAMPLE_SIZE} real system metric samples...")

for i in range(SAMPLE_SIZE):
    row = {
        "timestamp": datetime.now(),
        "cpu_percent": psutil.cpu_percent(interval=INTERVAL),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "net_sent_kb": psutil.net_io_counters().bytes_sent / 1024,
        "net_recv_kb": psutil.net_io_counters().bytes_recv / 1024
    }

    data.append(row)
    print(f"Sample {i+1}/{SAMPLE_SIZE} collected")

df = pd.DataFrame(data)

#  Write using absolute path
df.to_csv(CSV_PATH, index=False)

print("✅ Data collection complete")
print(f"📁 Saved to: {CSV_PATH}")
