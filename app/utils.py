import os
import pandas as pd
import streamlit as st

COUNTRY_CODES = {
    "Benin": "benin-malanville_clean.csv",
    "Sierra Leone": "sierraleone-bumbuna_clean.csv",
    "Togo": "togo-dapaong_qc_clean.csv"
}
METRICS = ["GHI", "DNI", "DHI", "WS", "WSgust", "Tamb", "RH"]

def load_country_data(selected_countries):
    dfs = {}
    for country in selected_countries:
        fname = COUNTRY_CODES.get(country)
        path = os.path.join("data", fname)
        if fname and os.path.exists(path):
            try:
                df = pd.read_csv(path)
                if not df.empty and any(col in df.columns for col in METRICS):
                    dfs[country] = df
            except Exception as e:
                st.warning(f"Failed to load {country}: {e}")
        else:
            st.warning(f"File for {country} not found in /data.")
    return dfs

def get_summary_stats(dfs, metric):
    stats = []
    for country, df in dfs.items():
        if metric in df:
            stats.append({
                "Country": country,
                "Mean": df[metric].mean(),
                "Median": df[metric].median(),
                "Std Dev": df[metric].std()
            })
    return pd.DataFrame(stats)