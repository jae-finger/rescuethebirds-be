from fastapi import APIRouter, Depends
from dotenv import load_dotenv
import os
from app.config import Settings, get_settings

# Load environment variables from .env file
load_dotenv()

router = APIRouter()

code_enviroment = os.getenv("CODE_ENVIRONMENT")


@router.get("/ping", include_in_schema=False)
async def pong(settings: Settings = Depends(get_settings)):
    return {"ping": "pong!", "environment": code_enviroment, "version": 1.1}
