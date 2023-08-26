import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.api import ping, forms  # Existing imports

log = logging.getLogger("uvicorn")

# Define a custom exception handler for 404 errors
async def custom_not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"message": "Womp womp -- not found."},
    )

def create_application() -> FastAPI:
    application = FastAPI()

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
