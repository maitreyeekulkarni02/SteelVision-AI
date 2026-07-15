"""
SteelVision AI
Industrial Live Sensor Dashboard
"""

import random

import streamlit as st

from ui.cards import metric_card


def show_sensors():

    st.subheader("LIVE INDUSTRIAL SENSORS")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card("Temperature", f"{random.randint(38,58)} ?C", "Normal", "#E53935")

    with c2:

        metric_card(
            "Pressure", f"{round(random.uniform(3.5,5.8),1)} bar", "Stable", "#1976D2"
        )

    with c3:

        metric_card("Motor RPM", str(random.randint(1180, 1320)), "Running", "#16C47F")

    with c4:

        metric_card("Power", f"{random.randint(14,22)} A", "Nominal", "#F5B700")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("Conveyor Belt Running")

    with c2:
        st.info("Camera Connected")

    with c3:
        st.warning("Next Inspection in 15 Minutes")
