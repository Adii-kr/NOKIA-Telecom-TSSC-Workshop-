# Importing libraries
import os
import time
import pandas as pd
import schedule
from datetime import datetime

# Setting up file paths
RAW_PATH = "telecom_raw.csv"
OUT_DIR = "output"
OUT_PATH = os.path.join(OUT_DIR, "telecom_cleaned.csv")
TMP_PATH = os.path.join(OUT_DIR, "telecom_cleaned.tmp.csv")
LOG_PATH = os.path.join(OUT_DIR, "etl_run.log")

# Create output folder
os.makedirs(OUT_DIR, exist_ok=True)


# Logging function
def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")
    print(f"[{ts}] {msg}")


# Data cleaning function
def clean_frame(df: pd.DataFrame) -> pd.DataFrame:

    # 1) Standardize text columns
    if "region" in df.columns:
        df["region"] = df["region"].astype(str).str.strip().str.title()

    # 2) Fill missing numeric values with median
    for col in ["data_used_gb", "calls_made", "revenue_inr"]:
        if col in df.columns:
            if not pd.api.types.is_numeric_dtype(df[col]):
                df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(df[col].median())

    # 3) Parse dates
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["date"] = df["date"].fillna(pd.Timestamp("2025-09-25"))

    # 4) Remove duplicates
    if {"customer_id", "date"}.issubset(df.columns):
        before = len(df)
        df = df.drop_duplicates(subset=["customer_id", "date"], keep="first")
        log(f"Deduplicated: removed {before - len(df)} duplicate row(s).")

    # 5) Clip invalid ranges
    if "data_used_gb" in df.columns:
        df["data_used_gb"] = df["data_used_gb"].clip(lower=0, upper=100)

    if "revenue_inr" in df.columns:
        df["revenue_inr"] = df["revenue_inr"].clip(lower=0)

    return df


# ETL Job Function
def etl_job():
    try:
        log("Starting ETL...")

        if not os.path.exists(RAW_PATH):
            log(f"Raw file not found: {RAW_PATH}")
            return

        # EXTRACT
        df = pd.read_csv(RAW_PATH)

        # TRANSFORM
        df = clean_frame(df)

        # LOAD
        df.to_csv(TMP_PATH, index=False)
        os.replace(TMP_PATH, OUT_PATH)

        log(f"ETL completed successfully. Rows written: {len(df)}.")

    except Exception as e:
        log(f"ETL failed: {e}")


# -------------------------------
# Scheduling (Classroom Demo)
# -------------------------------

schedule.clear()
schedule.every(10).seconds.do(etl_job)

runs = 3

print("Scheduler started...\n")

for _ in range(runs):
    schedule.run_pending()
    time.sleep(10)

print(f"\nDone. Scheduler exited after {runs} runs.")
