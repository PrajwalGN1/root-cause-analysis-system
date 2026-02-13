import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "system_metrics_anomaly.csv")

df = pd.read_csv(DATA_PATH)

st.title("Root Cause Analysis Dashboard")

fig, ax = plt.subplots(figsize=(5,5))
ax.plot(df["cpu_percent"], label="CPU")
ax.plot(df["memory_percent"], label="Memory")
ax.plot(df["disk_percent"], label="Disk")
ax.legend()

st.pyplot(fig)

st.subheader("Detected Anomalies")
st.dataframe(df[df["anomaly"] == -1])
