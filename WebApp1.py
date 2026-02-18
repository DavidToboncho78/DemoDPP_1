import streamlit as st
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

## -- Header section ---
st.title ("Better Together - DPP4.0 - Live Dynamic Battery DPP Demo")
st.subheader ("A demo with Catena-X, OPCF, IDTA, ECLASS,  Eclipse, ZVEI, VDMA,")
st.write ("i am passionate about basttery DPP ")
#st.image('PowerPointHMI - DPP Demo HMI2026_V2.jpg')
st.sidebar.title("Sidebar")
st.sidebar.markdown("This is a Stremlit sidebar...place holders")
st.link_button("Visit Complete Static DPP", "https://eds.worldeds.com/dpp/index.html#/dppDetailLocal?sn&passportId=EU240186EX2380002323&model=&partNum=01076608")
st.link_button("Visit Huawei Digital Power", "https://solar.huawei.com/de/products/luna2000-7-14-21-s1/")
def clicked():
            st.write('Clicked')
x = st.button("click Me", on_click=clicked)
st.write(x)
print(x)

#sliders to edit values 
myVoltage = st.slider("BESS Voltage",
                min_value=10,
                max_value=800,
                value=250,
                step=10,
                )
st.write(f"SoH:{myVoltage}")

mySoC = st.slider("BESS Stage of Charge",
                min_value=10,
                max_value=800,
                value=250,
                step=10,
                )
st.write(f"SoH:{mySoC}")

mySoH = st.slider("BESS Stat of health",
                min_value=10,
                max_value=800,
                value=250,
                step=10,
                )
st.write(f"SoH:{mySoH}")

