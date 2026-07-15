"""
SteelVision AI
Industrial Analytics Dashboard
"""

import streamlit as st

from utils.industrial_analytics import (
    defect_statistics,
    health_history,
    recent_activity,
)


def show_analytics_dashboard():

    st.title("Industrial Analytics Dashboard")

    st.divider()

    # ==========================
    # DEFECT ANALYTICS
    # ==========================

    st.subheader("Defect Distribution")

    defects = defect_statistics()

    if defects:

        st.bar_chart(defects)

    else:

        st.info("No defect data available")

    st.divider()

    # ==========================
    # HEALTH TREND
    # ==========================

    st.subheader("Machine Health Trend")

    history = health_history()

    if not history.empty:

        history = history.set_index("inspection_date")

        st.line_chart(history["health_score"])

    else:

        st.info("No health history available")

    st.divider()

    # ==========================
    # ACTIVITY TIMELINE
    # ==========================

    st.subheader("Recent Inspection Activity")

    activities = recent_activity()

    if activities:

        for item in activities:

            st.write("? " + item)

    else:

        st.info("No recent activity")
