import io

from fastapi import APIRouter, File, UploadFile
from PIL import Image

from database.database import SessionLocal
from database.machine_models import Machine
from utils.defect_engine import generate_industrial_defects
from utils.history import format_history, get_history
from utils.inspection import (
    calculate_health_score,
    get_machine_status,
    get_priority,
    get_recommendation,
)
from utils.model import detect_defects

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "SteelVision AI Backend",
    }


@router.post("/inspect")
async def inspect_machine(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes))

    result = detect_defects(image)

    defects = generate_industrial_defects(result["defects"])

    health = calculate_health_score(defects)

    status = get_machine_status(health)

    priority = get_priority(health)

    recommendation = get_recommendation(defects)

    return {
        "health_score": health,
        "status": status,
        "priority": priority,
        "defects": defects,
        "recommendation": recommendation,
    }


@router.get("/history")
def inspection_history():

    history = get_history()

    if history.empty:
        return []

    return format_history(history).to_dict(orient="records")


@router.get("/machines")
def get_machine_records():

    db = SessionLocal()

    machines = db.query(Machine).all()

    results = []

    for machine in machines:

        results.append(
            {
                "machine_id": machine.machine_id,
                "machine_name": machine.machine_name,
                "machine_type": machine.machine_type,
                "location": machine.location,
                "current_health": machine.current_health,
                "status": machine.status,
            }
        )

    db.close()

    return results
