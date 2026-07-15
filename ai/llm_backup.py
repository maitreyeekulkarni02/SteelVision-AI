"""
SteelVision AI
Local LLM Interface
"""

MODEL_NAME = "qwen2.5:3b"
from ollama import chat

from ai.prompts import SYSTEM_PROMPT


def ask_llm(context, question):

    response = chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context + "\n\nQuestion:\n" + question},
        ],
    )

    return response["message"]["content"]
