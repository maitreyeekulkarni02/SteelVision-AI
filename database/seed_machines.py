from database.database import SessionLocal
from database.machine_models import Machine


def seed():

    db = SessionLocal()

    machines = [
        Machine(
            machine_id="M001",
            machine_name="Hydraulic Press",
            machine_type="Press Machine",
            location="Production Line A",
            current_health=92,
            status="Healthy",
        ),
        Machine(
            machine_id="M002",
            machine_name="Conveyor System",
            machine_type="Conveyor",
            location="Assembly Area",
            current_health=76,
            status="Warning",
        ),
        Machine(
            machine_id="M003",
            machine_name="CNC Machine",
            machine_type="CNC",
            location="Manufacturing Bay",
            current_health=58,
            status="Warning",
        ),
        Machine(
            machine_id="M004",
            machine_name="Rolling Machine",
            machine_type="Rolling Mill",
            location="Steel Processing Unit",
            current_health=35,
            status="Critical",
        ),
    ]

    for machine in machines:

        exists = (
            db.query(Machine).filter(Machine.machine_id == machine.machine_id).first()
        )

        if not exists:

            db.add(machine)

    db.commit()

    db.close()

    print("Machines seeded successfully")


if __name__ == "__main__":
    seed()
