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

def kpi(card, title, value, note):
    with card:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.markdown(f"<div style='font-size:2rem; font-weight:700'>{value}</div>", unsafe_allow_html=True)
            st.caption(note)

kpi(c1, "Avg monthly cases", "245", "Mean across months (2009–2019)")
kpi(c2, "Peak year", "2018", "Highest annual average")
kpi(c3, "Seasonal peak", "May–July", "Typical outbreak window")
kpi(c4, "Coverage", "2009–2019", "Dataset period")

st.markdown("---")
