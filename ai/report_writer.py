"""
SteelVision AI
AI Maintenance Report Generator
"""

from ai.context import build_context
from ai.llm import ask_llm


def generate_ai_report(
    machine,
    defects,
    health,
    priority,
    recommendation,
):

    context = build_context(
        machine=machine,
        defects=defects,
        health=health,
        priority=priority,
        recommendation=recommendation,
    )

    question = """
Create a professional industrial maintenance report.

Include:

1. Executive Summary

2. Machine Health

3. Detected Defects

4. Root Cause Analysis

5. Risk Assessment

6. Maintenance Plan

7. Spare Parts Required

8. Preventive Recommendations

Keep it professional.
"""

    return ask_llm(
        context=context,
        question=question,
    )
