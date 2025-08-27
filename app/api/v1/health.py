from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "pg-hand FastAPI is up"}