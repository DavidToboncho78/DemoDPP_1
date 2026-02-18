import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Battery DPP Demo", page_icon=":tada:", layout="wide")

# 2. Header
st.title("Better Together - DPP4.0")
st.subheader("Live Dynamic Battery DPP Demo")
st.write("A demo with Catena-X, OPCF, IDTA, ECLASS, Eclipse, ZVEI, VDMA")

# 3. Sidebar
st.sidebar.title("Sidebar Navigation")
st.sidebar.info("This is a placeholder for DPP metadata.")

# 4. Links
st.link_button("Visit Complete Static DPP", "https://eds.worldeds.com/dpp/index.html#/dppDetailLocal?sn&passportId=EU240186EX2380002323&model=&partNum=01076608")
st.link_button("Visit Huawei Digital Power", "https://solar.huawei.com/de/products/luna2000-7-14-21-s1/")

# 5. Interactivity
if st.button("Click Me"):
    st.write('Button was clicked!')

st.divider()

# 6. Sliders (Units fixed for Voltage, SoC, and SoH)
myVoltage = st.slider("BESS Voltage", 10, 800, 250)
st.write(f"Current Voltage: {myVoltage} V")

mySoC = st.slider("BESS State of Charge", 0, 100, 50)
st.write(f"SoC: {mySoC} %")

mySoH = st.slider("BESS State of Health", 0, 100, 95)
st.write(f"SoH: {mySoH} %")
