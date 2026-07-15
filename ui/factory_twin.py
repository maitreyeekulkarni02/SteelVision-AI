"""
SteelVision AI
Factory Digital Twin Visualization
"""

import streamlit as st


def show_factory_twin():

    st.title("Factory Digital Twin")

    st.write("Live Industrial Machine Monitoring")

    st.divider()

    machines = [
        {"id": "M001", "health": 96, "status": "Healthy"},
        {"id": "M002", "health": 91, "status": "Healthy"},
        {"id": "M003", "health": 72, "status": "Warning"},
        {"id": "M004", "health": 38, "status": "Critical"},
    ]

    col1, col2 = st.columns(2)

    for index, machine in enumerate(machines):

        box = col1 if index % 2 == 0 else col2

        with box:

            if machine["health"] >= 80:

                icon = "??"

            elif machine["health"] >= 50:

                icon = "??"

            else:

                icon = "??"

            st.success(
                f"""
                {icon} {machine["id"]}


                Health:

                {machine["health"]}%


                Status:

                {machine["status"]}
                """
            )

    st.divider()

    st.subheader("Factory Intelligence")

    st.info(
        """
        AI Monitoring Active

        Critical machines:
        M004


        Recommended Action:

        Schedule preventive maintenance.
        """
    )
