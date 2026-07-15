"""
SteelVision AI
AI Copilot UI
"""

import streamlit as st

from ai.agent import ask_factory_ai


def show_copilot(
    machine,
    defects,
    health,
    priority,
    recommendation,
):

    st.subheader("🤖 SteelVision AI Copilot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask about this inspection...")

    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        history = [
            {
                "role": msg["role"],
                "content": msg["content"],
            }
            for msg in st.session_state.chat_history
        ]

        answer = ask_factory_ai(
            machine=machine,
            defects=defects,
            health=health,
            priority=priority,
            recommendation=recommendation,
            question=question,
            history=history[:-1],
        )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()
