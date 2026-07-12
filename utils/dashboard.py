"""
SteelVision AI
Industrial Dashboard Components
"""


import streamlit as st



# --------------------------------------------------
# MACHINE KPI CARDS
# --------------------------------------------------

def display_machine_metrics(
        health_score,
        status,
        priority,
        defect_count
):


    col1,col2,col3,col4 = st.columns(4)



    col1.metric(
        "Machine Health",
        f"{health_score}%"
    )


    col2.metric(
        "Condition",
        status
    )


    col3.metric(
        "Risk Level",
        priority
    )


    col4.metric(
        "Defects",
        defect_count
    )





# --------------------------------------------------
# INDUSTRIAL STATUS PANEL
# --------------------------------------------------

def display_status_panel(
        health_score,
        status
):


    st.subheader(
        "🏭 Machine Condition Monitoring"
    )


    if health_score >= 90:

        message = "🟢 Machine Operating Normally"


    elif health_score >= 70:

        message = "🟡 Maintenance Recommended"


    else:

        message = "🔴 Immediate Maintenance Required"



    st.info(
        message
    )


    st.progress(
        health_score/100
    )





# --------------------------------------------------
# EDGE AI STATUS
# --------------------------------------------------

def display_edge_status():


    st.subheader(
        "⚡ Edge AI System Status"
    )


    data = {

        "AI Engine":
        "YOLO Vision Model",


        "Processing":
        "Edge Device",


        "Inspection":
        "Real-Time",


        "System":
        "Online"

    }


    st.json(
        data
    )