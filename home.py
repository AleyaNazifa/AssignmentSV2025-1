import streamlit as st

st.title("🦠 Objective 1: Temporal & Seasonal Trend of HFMD in Malaysia (2009–2019)")
st.markdown("---")

st.subheader("🎯 Objective Statement")
st.write(
    "To analyze the **temporal trend** and **seasonal variation** of Hand, Foot and Mouth Disease (HFMD) cases "
    "in Malaysia from 2009 to 2019, identifying outbreak peaks and recurring seasonal patterns."
)

st.markdown("---")
st.subheader("📊 Summary Box")

# --- 3 Columns (Balanced layout) ---
col1, col2, col3 = st.columns(3, gap="large")

col1.metric(
    label="🦠 Average Monthly HFMD Cases",
    value="245",
    help="Mean number of HFMD cases per month across Malaysia (2009–2019)",
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

st.info(
    "This page summarizes the temporal trend of HFMD cases in Malaysia using historical data from 2009–2019. "
    "The average monthly cases were around **245**, with **2018** showing the highest outbreak intensity. "
    "Seasonal peaks occur primarily between **May and July**, reflecting Malaysia’s warm and humid period when HFMD spreads more easily."
)
