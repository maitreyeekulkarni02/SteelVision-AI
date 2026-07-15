from ai.context import build_context
from ai.llm import ask_llm

context = build_context(
    machine="M004",
    defects=[{"name": "Crack"}, {"name": "Oil Leakage"}, {"name": "Corrosion"}],
    health=38,
    priority="Immediate",
    recommendation="Replace bearing and inspect gearbox.",
)

answer = ask_llm(context, "Why is this machine critical?")

print(answer)
