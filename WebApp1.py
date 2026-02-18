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

# 5. Sliders to edit values 
st.divider() # Adds a nice visual line

myVoltage = st.slider("BESS Voltage", min_value=10, max_value=800, value=250, step=10)
st.write(f"Current Voltage: {myVoltage}V")

mySoC = st.slider("BESS State of Charge (SoC)", min_value=0, max_value=100, value=50, step=1)
st.write(f"SoC: {mySoC}%")

mySoH = st.slider("BESS State of Health (SoH)", min_value=0, max_value=100, value=95, step=1)
st.write(f"SoH: {mySoH}%")
