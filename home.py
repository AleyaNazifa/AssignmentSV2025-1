import streamlit as st

# --- PAGE TITLE ---
st.title("🦠 Objective 1: Temporal & Seasonal Trend of HFMD in Malaysia (2009–2019)")
st.markdown("---")

# --- OBJECTIVE STATEMENT ---
st.subheader("🎯 Objective Statement")
st.write(
    "To analyze the **temporal trend** and **seasonal variation** of Hand, Foot and Mouth Disease (HFMD) "
    "cases in Malaysia from 2009 to 2019, identifying outbreak peaks and recurring seasonal patterns."
)
st.markdown("---")

# --- SUMMARY BOX (3 METRICS) ---
st.subheader("📊 Summary Box")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="📈 Avg Monthly HFMD Cases",
    value="245",
    help="Mean number of HFMD cases per month across all Malaysian regions (2009–2019)",
    border=True
)

col2.metric(
    label="📅 Peak Outbreak Year",
    value="2018",
    help="Year with the highest recorded HFMD cases based on monthly averages",
    border=True
)

col3.metric(
    label="🌦️ Seasonal Peak Months",
    value="May – July",
    help="Months that consistently record the highest HFMD outbreaks each year",
    border=True
)

st.markdown("---")

# ===============================
# 📈 Objective 1 – Visualizations
# ===============================
import pandas as pd
import plotly.express as px

st.subheader("🧩 1) Data Loading & Monthly Preparation")

# GitHub raw CSV (you can change this to a file_uploader if you prefer)
DATA_URL = "https://raw.githubusercontent.com/AleyaNazifa/AssignmentSV2025-1/refs/heads/main/hfdm_data%20-%20Upload.csv"

@st.cache_data
def load_and_prepare_monthly(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    # normalize columns
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    # date parsing (CSV is dd/mm/yyyy)
    if "date" not in df.columns:
        raise ValueError("No 'Date' column found in the CSV.")
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date")

    # required HFMD region columns
    regions = ["southern", "northern", "central", "east_coast", "borneo"]
    missing = [c for c in regions if c not in df.columns]
    if missing:
        raise ValueError(f"Missing region columns: {missing}")

    # total cases per day
    df["total_cases"] = df[regions].sum(axis=1, numeric_only=True)

    # monthly aggregation
    df_m = (
        df.set_index("date")
          .resample("M")
          .mean(numeric_only=True)
          .reset_index()
          .rename(columns={"date": "Date"})
    )
    df_m["Year"] = df_m["Date"].dt.year
    df_m["Month"] = df_m["Date"].dt.month
    return df_m

try:
    df_m = load_and_prepare_monthly(DATA_URL)
    st.dataframe(df_m.head(), use_container_width=True)
    st.caption(f"Monthly rows: {len(df_m):,} • Years: {df_m['Year'].min()}–{df_m['Year'].max()}")
except Exception as e:
    st.error(f"❌ Unable to load/prepare dataset: {e}")
    st.stop()

st.markdown("---")

# --------------- Viz 1 ---------------
st.subheader("📉 2) Monthly HFMD Cases Trend")
fig_trend = px.line(
    df_m,
    x="Date", y="total_cases",
    title="Monthly Trend of HFMD Cases (2009–2019)",
    labels={"Date": "Year", "total_cases": "Average Monthly Cases"},
    line_shape="spline"
)
st.plotly_chart(fig_trend, use_container_width=True)
st.info("**Interpretation:** The time series shows **regular mid-year peaks** indicating a strong seasonal pattern in HFMD.")

st.markdown("---")

# --------------- Viz 2 ---------------
st.subheader("📊 3) Average Yearly HFMD Cases")
yearly_avg = df_m.groupby("Year")["total_cases"].mean().reset_index()
fig_year = px.bar(
    yearly_avg,
    x="Year", y="total_cases",
    title="Average Yearly HFMD Cases (2009–2019)",
    labels={"total_cases": "Average Monthly Cases"},
    color="total_cases",
    color_continuous_scale="Reds"
)
st.plotly_chart(fig_year, use_container_width=True)
st.info("**Interpretation:** Some years exhibit **higher baseline incidence**, highlighting periods that may need more resources/awareness.")

st.markdown("---")

# --------------- Viz 3 ---------------
st.subheader("🌡️ 4) Seasonal Pattern (Month × Year Heatmap)")
pivot = df_m.pivot_table(values="total_cases", index="Month", columns="Year", aggfunc="mean")
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

fig_heat = px.imshow(
    pivot,
    aspect="auto",
    origin="lower",
    color_continuous_scale="YlOrRd",
    labels=dict(x="Year", y="Month", color="Avg Monthly Cases"),
    title="Seasonal Heatmap of HFMD Cases"
)
fig_heat.update_yaxes(tickmode="array", tickvals=list(range(1,13)), ticktext=month_names)
st.plotly_chart(fig_heat, use_container_width=True)
st.info("**Interpretation:** Heatmap confirms **recurring surges in mid-year months**; intensity varies across years but the pattern is consistent.")

