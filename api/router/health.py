import time
from fastapi import APIRouter
from config import settings

router = APIRouter()
START_TIME = time.time()

@router.get("/api/health")
def health():
    return {
        "status": "ok",
        "model_loaded": False,  # Placeholder for actual model loading status
        "model_name": settings.model_name,
        "spacy_models": settings.spacy_models,
        "uptime_seconds": time.time() - START_TIME
    }