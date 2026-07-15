"""
SteelVision AI
Premium Metric Cards
"""

import streamlit as st


def metric_card(title, value, status, color="#1976D2"):

    st.markdown(
        f"""
    <div style="
        background:white;
        border-radius:18px;
        padding:20px;
        box-shadow:0 4px 18px rgba(0,0,0,.08);
        border-left:8px solid {color};
        margin-bottom:15px;
    ">

    <h4>{title}</h4>

    <h1>{value}</h1>

    <p style="color:{color};font-weight:bold;">
        {status}
    </p>

    </div>
    """,
        unsafe_allow_html=True,
    )
