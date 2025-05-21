import pandas as pd
import os

COUNTRY_CODES = {
    "Benin": "benin-malanville_clean.csv",
    "Sierra Leone": "sierraleone-bumbuna_clean.csv",
    "Togo": "togo-dapaong_qc_clean.csv"
}

def load_country_data(selected_countries):
    dfs = {}
    for country in selected_countries:
        fname = COUNTRY_CODES.get(country)
        path = os.path.join("data", fname)
        if os.path.exists(path):
            dfs[country] = pd.read_csv(path, parse_dates=True)
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