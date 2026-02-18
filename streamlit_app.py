import streamlit as st

st.title("Sanity Check")
st.write("If you can see this, the server is working!")

voltage = st.slider("Test Slider", 0, 100, 50)
st.write(f"Value is: {voltage}")
