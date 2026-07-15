"""
SteelVision AI
Local LLM Interface
"""

from ollama import chat

from ai.prompts import SYSTEM_PROMPT

MODEL_NAME = "qwen2.5:3b"


def ask_llm(context, question, history=None):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    if history:
        messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": (context + "\n\nQuestion:\n" + question),
        }
    )

    response = chat(
        model=MODEL_NAME,
        messages=messages,
    )

    return response["message"]["content"]
