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

# 💅 make metric cards pretty
st.markdown("""
<style>
/* card look for st.metric */
div[data-testid="stMetric"] {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(250,250,250,0.15);
  border-radius: 14px;
  padding: 16px 18px;
}
div[data-testid="stMetric"] > label {
  font-weight: 600 !important;
  opacity: 0.9;
}
div[data-testid="stMetricValue"] > div {
  font-size: 2rem !important;  /* make the number bigger */
  font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)


# --- SUMMARY BOX (METRIC CARDS) ---
st.subheader("📊 Summary Box")
c1, c2, c3, c4 = st.columns(4, gap="medium")

c1.metric(
    label="Avg Monthly Cases",
    value="245",
    help="Mean monthly HFMD cases across Malaysia (2009–2019)",
    border=True,
)

c2.metric(
    label="Peak Year",
    value="2018",
    help="Year with the highest average monthly HFMD cases",
    border=True,
)

c3.metric(
    label="Seasonal Peak",
    value="May–Jul",
    help="Months that most often record the highest HFMD activity",
    border=True,
)

c4.metric(
    label="Coverage",
    value="2009–2019",
    help="Temporal coverage of the dataset used in this page",
    border=True,
)
st.markdown("---")
