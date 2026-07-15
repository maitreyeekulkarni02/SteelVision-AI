"""
SteelVision AI
Industrial Dashboard
"""

import streamlit as st

from ui.cards import metric_card
from ui.components import section


def show_dashboard():

    section(
        "STEELVISION AI COMMAND CENTER", "Industry 4.0 Edge AI Industrial Monitoring"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Plant Health", "92%", "Excellent", "#16C47F")

    with c2:
        metric_card("Critical Alerts", "2", "Immediate Action", "#E53935")

    with c3:
        metric_card("Maintenance Due", "5", "Scheduled", "#F5B700")

    with c4:
        metric_card("AI Accuracy", "96.8%", "YOLO Active", "#1976D2")

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        st.subheader("FACTORY OVERVIEW")

        machines = [
            ("M001", "Healthy", "92%"),
            ("M002", "Healthy", "89%"),
            ("M003", "Warning", "71%"),
            ("M004", "Critical", "38%"),
            ("M005", "Healthy", "95%"),
        ]

        for m, s, h in machines:

            color = "Healthy"

            if s == "Warning":
                color = "Healthy"

            if s == "Critical":
                color = "Healthy"

            st.markdown(
                f"""
**{color} {m}**

Health : **{h}**

Status : **{s}**

---
"""
            )

    with right:

        st.subheader("NOTIFICATIONS")

        st.success("Inspection Complete")

        st.info("Camera Connected")

        st.warning("Machine M004 Warning")

        st.success("Report Generated")

        st.subheader("MAINTENANCE")

        st.write("Today")

        st.write("? Machine M004")

        st.write("Tomorrow")

        st.write("? Machine M003")

        st.write("Friday")

        st.write("? Machine M002")
