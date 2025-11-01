import streamlit as st

# --- PAGE TITLE ---
st.title("🦠 Objective 1: Temporal & Seasonal Trend of HFMD in Malaysia (2009–2019)")
st.markdown("---")

# --- OBJECTIVE STATEMENT ---
st.subheader("🎯 Objective Statement")
st.write(
    "To analyze the **temporal trend** and **seasonal variation** of Hand, Foot and Mouth Disease (HFMD) cases "
    "in Malaysia from 2009 to 2019, identifying outbreak peaks and recurring seasonal patterns."
)

st.markdown("---")

# --- better metric card styling ---
st.markdown("""
<style>
/* container styling for each metric */
div[data-testid="stMetric"] {
  background-color: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 12px;
  padding: 18px;
  margin: 6px;
  min-width: 230px;
  height: 120px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

/* label styling */
div[data-testid="stMetric"] > label {
  white-space: normal !important;
  word-wrap: break-word !important;
  font-weight: 600 !important;
  font-size: 0.95rem !important;
  opacity: 0.9 !important;
  line-height: 1.2rem !important;
  text-align: center !important;
}

/* value styling */
div[data-testid="stMetricValue"] > div {
  font-size: 1.9rem !important;
  font-weight: 700 !important;
  color: #fafafa !important;
  margin-top: 4px;
  text-align: center !important;
}
</style>
""", unsafe_allow_html=True)

# --- summary metrics ---
st.subheader("📊 Summary Box")
c1, c2, c3, c4 = st.columns(4, gap="large")

c1.metric(
    label="Avg monthly cases",
    value="245",
    help="Mean HFMD cases per month across all regions (2009–2019)",
    border=True,
)
c1.caption("Mean across all months")

c2.metric(
    label="Peak year",
    value="2018",
    help="Year with the highest average monthly HFMD cases",
    border=True,
)
c2.caption("Highest annual average")

c3.metric(
    label="Seasonal peak",
    value="May–July",
    help="Months that most often recorded the highest HFMD activity",
    border=True,
)
c3.caption("Typical outbreak window")

c4.metric(
    label="Coverage",
    value="2009–2019",
    help="Temporal coverage of the dataset",
    border=True,
)
c4.caption("Dataset period")
st.markdown("---")

