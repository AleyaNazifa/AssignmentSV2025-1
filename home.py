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

st.markdown("""
<style>
/* make metrics wider and text wrap cleanly */
div[data-testid="stMetric"] {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(250,250,250,0.15);
  border-radius: 14px;
  padding: 18px 22px;
  min-width: 210px;
  height: 110px;
  word-wrap: break-word !important;
  overflow-wrap: break-word !important;
}
div[data-testid="stMetric"] > label {
  white-space: normal !important;
  text-align: center !important;
  display: block;
  font-size: 0.95rem !important;
  line-height: 1.2rem !important;
}
div[data-testid="stMetricValue"] > div {
  font-size: 1.8rem !important;
  text-align: center !important;
}
</style>
""", unsafe_allow_html=True)


st.subheader("📊 Summary Box")
c1, c2, c3, c4 = st.columns(4, gap="large")

c1.metric(
    label="Average Monthly HFMD Cases",
    value="245",
    help="Mean monthly HFMD cases across Malaysia (2009–2019)",
    border=True,
)
c2.metric(
    label="Peak Outbreak Year",
    value="2018",
    help="Year with the highest average monthly HFMD cases",
    border=True,
)
c3.metric(
    label="Seasonal Peak Months",
    value="May – July",
    help="Months that record the highest HFMD activity each year",
    border=True,
)
c4.metric(
    label="Dataset Coverage Period",
    value="2009 – 2019",
    help="Time range covered by the HFMD dataset",
    border=True,
)
st.markdown("---")
