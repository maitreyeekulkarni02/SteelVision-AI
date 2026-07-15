import streamlit as st

from utils.history import format_history, get_history


def show_history():

    st.success("History page loaded successfully!")

    st.title("Inspection History")

    records = get_history()

    st.write("Rows found:", len(records))

    if not records.empty:

        history = format_history(records)

        st.dataframe(history, width="stretch")

    else:

        st.info("No inspection records found.")
