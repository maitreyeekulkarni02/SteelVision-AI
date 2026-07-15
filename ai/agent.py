"""
SteelVision AI
AI Agent
"""

from ai.context import build_context
from ai.llm import ask_llm


def ask_factory_ai(
    machine,
    defects,
    health,
    priority,
    recommendation,
    question,
    history=None,
):
    context = build_context(
        machine=machine,
        defects=defects,
        health=health,
        priority=priority,
        recommendation=recommendation,
    )

    return ask_llm(
        context=context,
        question=question,
        history=history,
    )
