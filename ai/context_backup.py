"""
SteelVision AI
Context Builder
"""


def build_context(machine, defects, health, priority, recommendation):
    """
    Convert inspection results into
    a prompt context for the AI.
    """

    defect_names = []

    for defect in defects:

        if isinstance(defect, dict):

            defect_names.append(defect.get("name", "Unknown"))

        else:

            defect_names.append(str(defect))

    context = f"""
Machine ID:
{machine}

Machine Health:
{health}%

Detected Defects:
{", ".join(defect_names)}

Maintenance Priority:
{priority}

Recommendation:
{recommendation}
"""

    return context
