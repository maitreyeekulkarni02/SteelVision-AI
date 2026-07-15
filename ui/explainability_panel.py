import streamlit as st


def show_explanation(data):

    st.subheader("AI Decision Explanation")

    st.info(
        f"""
        Risk Level:

        {data["risk"]}


        Reason:

        {data["reason"]}
        """
    )

    st.write("Risk Factors:")

    for factor in data["factors"]:

        st.warning(factor)
