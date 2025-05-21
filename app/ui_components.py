import streamlit as st
import plotly.express as px
import pandas as pd
from utils import COUNTRY_CODES, METRICS, get_summary_stats

PLOT_TYPES = ["Line", "Boxplot", "Histogram", "Scatter"]
COLORS = px.colors.qualitative.Dark24

def country_selector():
    return st.multiselect(
        "Select countries to compare",
        list(COUNTRY_CODES.keys()),
        default=list(COUNTRY_CODES.keys())
    )

def metric_selector():
    return st.selectbox(
        "Select metric",
        METRICS
    )

def plot_type_selector():
    return st.selectbox(
        "Select plot type",
        PLOT_TYPES
    )

def individual_plots_section(dfs, metric, plot_type):
    st.markdown("### Individual Country Trends")
    if not dfs:
        st.info("Please select at least one country.")
        return
    tabs = st.tabs(list(dfs.keys()))
    for i, (country, df) in enumerate(dfs.items()):
        with tabs[i]:
            if metric in df:
                if plot_type == "Line":
                    fig = px.line(
                        df,
                        y=metric,
                        title=f"{country} - {metric} Trend",
                        markers=True,
                        template="plotly_white",
                        color_discrete_sequence=[COLORS[i % len(COLORS)]]
                    )
                    fig.update_traces(line=dict(width=3))
                elif plot_type == "Boxplot":
                    fig = px.box(
                        df,
                        y=metric,
                        title=f"{country} - {metric} Boxplot",
                        template="plotly_white",
                        color_discrete_sequence=[COLORS[i % len(COLORS)]]
                    )
                elif plot_type == "Histogram":
                    fig = px.histogram(
                        df,
                        x=metric,
                        title=f"{country} - {metric} Histogram",
                        template="plotly_white",
                        color_discrete_sequence=[COLORS[i % len(COLORS)]],
                        nbins=30
                    )
                elif plot_type == "Scatter":
                    fig = px.scatter(
                        df,
                        y=metric,
                        x=df.index,
                        title=f"{country} - {metric} Scatter",
                        template="plotly_white",
                        color_discrete_sequence=[COLORS[i % len(COLORS)]]
                    )
                else:
                    st.warning("Unsupported plot type.")
                    continue
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info(f"No data for {metric} in {country}.")

def comparison_plot_section(dfs, metric, plot_type):
    st.markdown("### Comparison Across Countries")
    data = []
    for country, df in dfs.items():
        if metric in df:
            temp = df[[metric]].copy()
            temp["Country"] = country
            temp["Index"] = temp.index
            data.append(temp)
    if not data:
        st.info("No data available for comparison.")
        return
    plot_df = pd.concat(data)
    if plot_type == "Line":
        fig = px.line(
            plot_df,
            x="Index",
            y=metric,
            color="Country",
            title=f"{metric} Comparison",
            markers=True,
            template="plotly_white",
            color_discrete_sequence=COLORS
        )
        fig.update_traces(line=dict(width=3))
    elif plot_type == "Boxplot":
        fig = px.box(
            plot_df,
            x="Country",
            y=metric,
            color="Country",
            title=f"{metric} Boxplot Comparison",
            template="plotly_white",
            color_discrete_sequence=COLORS
        )
    elif plot_type == "Histogram":
        fig = px.histogram(
            plot_df,
            x=metric,
            color="Country",
            barmode="overlay",
            nbins=30,
            title=f"{metric} Histogram Comparison",
            template="plotly_white",
            color_discrete_sequence=COLORS
        )
    elif plot_type == "Scatter":
        fig = px.scatter(
            plot_df,
            x="Index",
            y=metric,
            color="Country",
            title=f"{metric} Scatter Comparison",
            template="plotly_white",
            color_discrete_sequence=COLORS
        )
    else:
        st.warning("Unsupported plot type.")
        return
    st.plotly_chart(fig, use_container_width=True)

def summary_table(dfs, metric):
    st.subheader(f"Summary Table: {metric}")
    stats_df = get_summary_stats(dfs, metric)
    st.dataframe(stats_df, use_container_width=True)

def observations_section(dfs, metric, plot_type):
    st.subheader("Key Observations")
    st.markdown(f"""
    - Current view: **{plot_type}** for **{metric}**.
    - Explore individual country trends above, and compare all countries below.
    - Use different plot types and metrics to discover deeper insights!
    """)