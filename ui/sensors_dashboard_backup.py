"""
SteelVision AI
Live Sensor Dashboard
"""

import streamlit as st

from utils.sensors import get_sensor_data


def sensor_status(value, warning, critical):

    if value >= critical:
        return "??"

    if value >= warning:
        return "??"

    return "??"


def show_sensor_dashboard():

    st.title("Live Industrial Sensors")

    st.caption("Real-Time Machine Telemetry (Simulation)")

    data = get_sensor_data()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Temperature", f'{data["temperature"]} ?C')

        st.write(sensor_status(data["temperature"], 70, 80))

        st.metric("Pressure", f'{data["pressure"]} bar')

    with c2:

        st.metric("Vibration", f'{data["vibration"]} mm/s')

        st.write(sensor_status(data["vibration"], 4, 6))

        st.metric("RPM", data["rpm"])

    with c3:

        st.metric("Motor Current", f'{data["current"]} A')

        st.metric("Voltage", f'{data["voltage"]} V')

    st.divider()

    if data["temperature"] >= 80 or data["vibration"] >= 6:

        st.error(
            "? AI Alert: Abnormal machine behaviour detected. Preventive maintenance recommended."
        )

    else:

        st.success("Machine operating within normal parameters.")
