"""
SteelVision AI
Executive Command Center
"""

from datetime import datetime

import streamlit as st

from ui.explainability_panel import show_explanation
from utils.command_data import get_command_metrics
from utils.explainability import explain_prediction
from utils.predictive import predict_failure
from utils.risk_analyzer import get_highest_risk_machine


def show_command_center():

    st.markdown(
        """
        <h1>
        STEELVISION AI COMMAND CENTER
        </h1>

        <p>
        Industry 4.0 Edge AI Predictive Maintenance Platform
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # KPI SECTION

    data = get_command_metrics()

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric("Plant Health", f"{data['plant_health']}%")

    with c2:
        st.metric("Machines", data["machines"])

    with c3:
        st.metric("Critical Alerts", data["critical"])

    with c4:
        st.metric("AI Accuracy", f"{data['ai_accuracy']}%")

    with c5:
        st.metric("Reports", data["reports"])

    st.divider()

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Factory Overview")

        machines = [
            ("M001", "Healthy", "96%"),
            ("M002", "Healthy", "91%"),
            ("M003", "Warning", "72%"),
            ("M004", "Critical", "38%"),
            ("M005", "Healthy", "95%"),
        ]

        for name, status, health in machines:

            st.write(
                f"""
                **{name}**

                Status : {status}

                Health : {health}

                ---
                """
            )

    with right:

        st.subheader("AI Recommendation")

        risk_machine = get_highest_risk_machine()

        prediction = predict_failure(
            health=risk_machine["health"], defect_count=risk_machine["defects"]
        )

        st.warning(
            f"""
            Machine:

            {risk_machine["machine"]}


            Current Health:

            {risk_machine["health"]}%


            Detected Defects:

            {risk_machine["defects"]}


            Failure Probability:

            {prediction["failure_probability"]}%


            Maintenance Priority:

            {prediction["priority"]}


            Risk Level:

            {prediction["risk"]}


            Estimated Repair Cost:

            Rs. {prediction["estimated_cost"]}


            Recommended Action:

            Schedule preventive maintenance immediately.
            """
        )

        # ================================
        # AI EXPLAINABILITY PANEL
        # ================================

        explanation = explain_prediction(
            health=risk_machine["health"],
            defect_count=risk_machine["defects"],
            failure_probability=prediction["failure_probability"],
        )

        show_explanation(explanation)

        st.subheader("Recent Activity")

        activities = [
            "Inspection completed",
            "Defect detected",
            "Health updated",
            "Report generated",
        ]

        for item in activities:

            st.write(datetime.now().strftime("%H:%M"), item)
