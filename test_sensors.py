import streamlit as st

from ui.sensors import show_sensors

st.set_page_config(layout="wide")

st.title("Industrial Sensors Demo")

show_sensors()
