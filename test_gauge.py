import streamlit as st

from ui.gauges import health_gauge

st.title("Gauge Test")

health_gauge(92, "Plant Health")

health_gauge(71, "Machine M003")

health_gauge(38, "Machine M004")
