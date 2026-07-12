"""
SteelVision AI
Inspection History Manager

Handles saving and retrieving inspection records.
"""

from database.database import SessionLocal
from database.models import InspectionHistory

import json



# --------------------------------------------------
# SAVE INSPECTION RECORD
# --------------------------------------------------

def save_inspection(
        machine_name,
        defects,
        health_score,
        status,
        priority,
        recommendation
):


    db = SessionLocal()


    try:

        record = InspectionHistory(

            machine_name=machine_name,

            defects=json.dumps(
                defects
            ),

            health_score=health_score,

            machine_status=status,

            maintenance_priority=priority,

            recommendation=recommendation
        )


        db.add(record)

        db.commit()

        db.refresh(record)


        return record



    finally:

        db.close()



# --------------------------------------------------
# GET INSPECTION HISTORY
# --------------------------------------------------

def get_history(limit=20):


    db = SessionLocal()


    try:

        records = (
            db.query(
                InspectionHistory
            )
            .order_by(
                InspectionHistory.id.desc()
            )
            .limit(limit)
            .all()
        )


        return records


    finally:

        db.close()



# --------------------------------------------------
# CONVERT DATABASE RECORD
# --------------------------------------------------

def format_history(records):


    history=[]


    for item in records:

        history.append({

            "Machine":
            item.machine_name,


            "Date":
            str(item.inspection_time),


            "Health Score":
            item.health_score,


            "Status":
            item.machine_status,


            "Priority":
            item.maintenance_priority,


            "Recommendation":
            item.recommendation

        })


    return history