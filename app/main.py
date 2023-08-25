import logging
from app.api import ping, forms
from fastapi import FastAPI


log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()

    # Routes
    application.include_router(forms.router, prefix="/forms", tags=["forms"])
    application.include_router(ping.router)
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
