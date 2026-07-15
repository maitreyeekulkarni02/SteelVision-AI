"""
SteelVision AI
Reusable UI Components
"""

import streamlit as st


def section(title, subtitle=""):

    st.markdown(
        f"""
    <div style="padding:15px 0;">
        <h2 style="margin-bottom:0;">{title}</h2>
        <p style="color:gray;">{subtitle}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


def divider():

    st.markdown("<hr>", unsafe_allow_html=True)


def success(msg):

    st.success(msg)


def warning(msg):

    st.warning(msg)


def error(msg):

    st.error(msg)


def info(msg):

    st.info(msg)
