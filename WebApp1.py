import streamlit as st

st.set_page_config(page_title="Battery DPP Demo", layout="wide")

st.title("Better Together - DPP4.0")
st.subheader("Live Dynamic Battery DPP Demo")

st.sidebar.title("Navigation")
st.sidebar.info("DPP Demo 2026")

# Links
st.link_button("Visit Complete Static DPP", "https://eds.worldeds.com/dpp/index.html#/dppDetailLocal?sn&passportId=EU240186EX2380002323&model=&partNum=01076608")
st.link_button("Visit Huawei Digital Power", "https://solar.huawei.com/de/products/luna2000-7-14-21-s1/")

# Sliders
v = st.slider("BESS Voltage", 10, 800, 250)
soc = st.slider("State of Charge (%)", 0, 100, 50)
soh = st.slider("State of Health (%)", 0, 100, 95)

st.write(f"Telemetry: {v}V | SoC: {soc}% | SoH: {soh}%")
