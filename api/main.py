from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="SteelVision AI API",
    description="Industrial Edge AI Inspection Backend",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "SteelVision AI Backend Running",
        "status": "OK",
    }
