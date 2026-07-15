"""
SteelVision AI
Professional Gauge Charts
"""

import plotly.graph_objects as go
import streamlit as st


def health_gauge(value=90, title="Machine Health"):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#1976D2"},
                "steps": [
                    {"range": [0, 40], "color": "#F44336"},
                    {"range": [40, 70], "color": "#FFC107"},
                    {"range": [70, 100], "color": "#4CAF50"},
                ],
                "threshold": {"line": {"color": "black", "width": 4}, "value": value},
            },
        )
    )

    fig.update_layout(height=320, margin=dict(l=20, r=20, t=40, b=20))

    st.plotly_chart(fig, use_container_width=True)
