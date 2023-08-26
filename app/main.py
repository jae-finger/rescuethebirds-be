import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.api import ping, forms  # Existing imports
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

log = logging.getLogger("uvicorn")


# Define a custom exception handler for 404 errors
async def custom_not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"message": "Womp womp -- not found."},
    )


def create_application() -> FastAPI:
    application = FastAPI()

    # Read allowed origins from .env file
    allowed_origins = [os.getenv("ALLOWED_ORIGIN")]

    # Add CORS middleware
    application.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,  # List of allowed origins read from .env
        allow_credentials=True,  # Allow cookies to be sent with request
        allow_methods=["*"],  # Allow all methods
        allow_headers=["*"],  # Allow all headers
    )

    # Register the custom exception handler
    application.add_exception_handler(404, custom_not_found_handler)

    # Existing routes
    application.include_router(forms.router, prefix="/forms", tags=["forms"])
    application.include_router(ping.router)

    return application


app = create_application()


# Existing startup and shutdown events
@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
