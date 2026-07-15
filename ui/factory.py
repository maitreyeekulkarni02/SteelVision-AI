"""
SteelVision AI
Factory Digital Twin
"""

import streamlit as st


def machine_box(name, status, health, line):

    colors = {"Healthy": "#16C47F", "Warning": "#F5B700", "Critical": "#E53935"}

    icons = {"Healthy": "Healthy", "Warning": "Healthy", "Critical": "Healthy"}

    color = colors.get(status, "#1976D2")
    icon = icons.get(status, "?")

    st.markdown(
        f"""
<div style="
background:white;
border-left:8px solid {color};
padding:18px;
border-radius:15px;
box-shadow:0 4px 18px rgba(0,0,0,.08);
margin-bottom:18px;
">

<h4>{icon} {name}</h4>

<b>Production Line</b><br>
{line}

<br><br>

<b>Health</b>

{health}%

<br>

<b>Status</b>

{status}

</div>
""",
        unsafe_allow_html=True,
    )


def show_factory():

    st.markdown("## FACTORY DIGITAL TWIN")

    st.caption("Real-Time Industrial Machine Overview")

    row1 = st.columns(3)

    with row1[0]:
        machine_box("Machine M001", "Healthy", 96, "Assembly Line")

    with row1[1]:
        machine_box("Machine M002", "Healthy", 91, "Assembly Line")

    with row1[2]:
        machine_box("Machine M003", "Warning", 72, "Assembly Line")

    row2 = st.columns(3)

    with row2[0]:
        machine_box("Machine M004", "Critical", 39, "Packaging")

    with row2[1]:
        machine_box("Machine M005", "Healthy", 95, "Packaging")

    with row2[2]:
        machine_box("Machine M006", "Healthy", 94, "Warehouse")

    st.markdown("---")

    st.success("Healthy Machines : 4")

    st.warning("Warning Machines : 1")

    st.error("Critical Machines : 1")
