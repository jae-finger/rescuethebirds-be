from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings), include_in_schema=False):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
