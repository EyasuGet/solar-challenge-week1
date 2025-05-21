import streamlit as st
from utils import load_country_data, COUNTRY_CODES, METRICS
from ui_components import (
    country_selector,
    metric_selector,
    plot_type_selector,
    individual_plots_section,
    comparison_plot_section,
    summary_table,
    observations_section
)

st.set_page_config(
    page_title="Solar Country Comparison Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Country Comparison Dashboard")
st.markdown("""
This dashboard lets you compare solar resource metrics across Benin, Sierra Leone, and Togo.
Select countries, metrics, and plot types below to visualize and compare.
""")

# ---- UI Controls ----
with st.container():
    selected_countries = country_selector()
    col1, col2 = st.columns(2)
    with col1:
        selected_metric = metric_selector()
    with col2:
        selected_plot = plot_type_selector()
    st.caption("Data is loaded from local cleaned CSV")

# ---- Load Data ----
dfs = load_country_data(selected_countries)

# ---- Plots ----
if dfs:
    individual_plots_section(dfs, selected_metric, selected_plot)
    comparison_plot_section(dfs, selected_metric, selected_plot)
else:
    st.info("No data loaded. Please check your country selections and CSV files in /data.")

# ---- Summary and Observations ----
summary_table(dfs, selected_metric)
observations_section(dfs, selected_metric, selected_plot)