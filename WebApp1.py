import streamlit as st

st.set_page_config(page_title="Battery DPP Demo", layout="wide")

st.title("Better Together - DPP4.0")
st.subheader("Live Dynamic Battery DPP Demo")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.info("Battery Passport Demo 2026")

# Sliders
v = st.slider("BESS Voltage", 10, 800, 250)
soc = st.slider("State of Charge", 0, 100, 80)
soh = st.slider("State of Health", 0, 100, 95)

st.write(f"Telemetry: {v}V | SoC: {soc}% | SoH: {soh}%")
