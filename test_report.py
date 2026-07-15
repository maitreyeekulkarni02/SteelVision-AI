from ai.report_writer import generate_ai_report

report = generate_ai_report(
    machine="M004",
    defects=[
        {"name": "Crack"},
        {"name": "Corrosion"},
        {"name": "Oil Leakage"},
    ],
    health=38,
    priority="Immediate",
    recommendation="Replace bearing and inspect gearbox.",
)

print(report)
