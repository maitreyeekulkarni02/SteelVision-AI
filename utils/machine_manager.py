"""
SteelVision AI
Machine Manager

Handles industrial machine records.
"""


from database.database import SessionLocal
from database.machine_models import Machine

from datetime import datetime



# ======================================
# ADD MACHINE
# ======================================

def add_machine(
        machine_id,
        machine_name,
        machine_type,
        location,
        installation_date
):


    db = SessionLocal()


    try:

        machine = Machine(

            machine_id=machine_id,

            machine_name=machine_name,

            machine_type=machine_type,

            location=location,

            installation_date=installation_date,

            current_health=100,

            status="Excellent"

        )


        db.add(machine)

        db.commit()

        db.refresh(machine)


        return machine


    finally:

        db.close()



# ======================================
# GET ALL MACHINES
# ======================================

def get_machines():


    db = SessionLocal()


    try:

        machines = (
            db.query(Machine)
            .all()
        )


        return machines


    finally:

        db.close()



# ======================================
# UPDATE MACHINE HEALTH
# ======================================

def update_machine_health(

        machine_id,

        health,

        status

):


    db = SessionLocal()


    try:


        machine = (

            db.query(Machine)

            .filter(
                Machine.machine_id == machine_id
            )

            .first()

        )


        if machine:


            machine.current_health = health

            machine.status = status

            machine.last_inspection = datetime.utcnow()


            db.commit()



        return machine



    finally:

        db.close()