import streamlit as st

# 1. Page Config
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# 2. Header Section
st.title("Better Together - DPP4.0 - Live Dynamic Battery DPP Demo")
st.subheader("A demo with Catena-X, OPCF, IDTA, ECLASS, Eclipse, ZVEI, VDMA")
st.write("I am passionate about battery DPP")

# 3. Sidebar
st.sidebar.title("Sidebar")
st.sidebar.markdown("This is a Streamlit sidebar... placeholders")

# 4. Buttons
st.link_button("Visit Complete Static DPP", "https://eds.worldeds.com/dpp/index.html#/dppDetailLocal?sn&passportId=EU240186EX2380002323&model=&partNum=01076608")
st.link_button("Visit Huawei Digital Power", "https://solar.huawei.com/de/products/luna2000-7-14-21-s1/")

if st.button("Click Me"):
    st.write('Button was clicked!')

# Sliders to edit values
st.header("Live Battery Telemetry")

col1, col2, col3 = st.columns(3)

with col1:
    myVoltage = st.slider("BESS Voltage", 10, 800, 250)
    st.metric("Voltage", f"{myVoltage} V")

with col2:
    mySoC = st.slider("State of Charge", 0, 100, 80)
    st.metric("SoC", f"{mySoC} %")

with col3:
    mySoH = st.slider("State of Health", 0, 100, 98)
    st.metric("SoH", f"{mySoH} %")
