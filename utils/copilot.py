"""
SteelVision AI
Industrial AI Copilot
"""

from database.database import SessionLocal
from database.machine_models import Machine
from database.models import InspectionHistory


def ask_copilot(question: str):

    db = SessionLocal()

    q = question.lower()

    try:

        if "critical" in q:

            machines = db.query(Machine).filter(Machine.status == "Critical").all()

            if not machines:
                return "No critical machines found."

            response = "=== CRITICAL MACHINES ===\n\n"

            for m in machines:

                response += (
                    f"Machine ID : {m.machine_id}\n"
                    f"Machine : {m.machine_name}\n"
                    f"Health : {m.current_health}%\n"
                    f"Location : {m.location}\n\n"
                )

            return response

        elif "history" in q:

            total = db.query(InspectionHistory).count()

            return f"Total inspections stored : {total}"

        elif "health" in q:

            machine = db.query(Machine).order_by(Machine.current_health.asc()).first()

            if machine:

                return (
                    f"Lowest health machine is "
                    f"{machine.machine_id} "
                    f"({machine.machine_name}) "
                    f"with health "
                    f"{machine.current_health}%."
                )

            return "No machine data available."

        elif "maintenance" in q:

            return "Immediate maintenance is recommended " "for all Critical machines."

        elif "summary" in q:

            total = db.query(InspectionHistory).count()

            critical = db.query(Machine).filter(Machine.status == "Critical").count()

            return (
                f"Factory Summary\n\n"
                f"Machines needing attention : {critical}\n"
                f"Total inspections : {total}"
            )

        else:

            return (
                "I can answer:\n\n"
                "- Critical machines\n"
                "- Machine health\n"
                "- Maintenance\n"
                "- Inspection history\n"
                "- Factory summary"
            )

    finally:

        db.close()
