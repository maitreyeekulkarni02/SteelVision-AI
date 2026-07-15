"""
SteelVision AI
Maintenance Planner UI
"""

import streamlit as st


def show_maintenance_plan(plan):

    st.subheader("AI Maintenance Planner")

    c1, c2 = st.columns(2)

    with c1:

        st.metric("Priority", plan["priority"])

        st.metric("Estimated Repair", f'{plan["hours"]} Hours')

        st.metric("Maintenance Team", plan["team"])

    with c2:

        st.metric("Estimated Cost", f'Rs. {plan["cost"]:,}')

        st.write("### Required Parts")

        for part in plan["parts"]:

            st.write(f"? {part}")

    st.divider()

    st.write("### Maintenance Checklist")

    for i, step in enumerate(plan["steps"], start=1):

        st.checkbox(f"{i}. {step}", value=False, key=f"maint_{i}")
