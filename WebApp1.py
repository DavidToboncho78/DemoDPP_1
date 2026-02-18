import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.title("Better Together - DPP4.0 - Live Dynamic Battery DPP Demo")
st.subheader("A demo with Catena-X, OPCF, IDTA, ECLASS, Eclipse, ZVEI, VDMA")
st.write("I am passionate about battery DPP")

# Side bar
st.sidebar.title("Sidebar")
st.sidebar.markdown("This is a Streamlit sidebar... placeholders")

# Links
st.link_button("Visit Complete Static DPP", "https://eds.worldeds.com/dpp/index.html#/dppDetailLocal?sn&passportId=EU240186EX2380002323&model=&partNum=01076608")
st.link_button("Visit Huawei Digital Power", "https://solar.huawei.com/de/products/luna2000-7-14-21-s1/")

# Interactivity
if st.button("Click Me"):
    st.write('Clicked')

# Sliders
st.divider()
myVoltage = st.slider("BESS Voltage", 10, 800, 250, 10)
st.write(f"Voltage: {myVoltage}V")

mySoC = st.slider("BESS State of Charge", 0, 100, 50, 1)
st.write(f"SoC: {mySoC}%")

mySoH = st.slider("BESS State of Health", 0, 100, 95, 1)
st.write(f"SoH: {mySoH}%")
