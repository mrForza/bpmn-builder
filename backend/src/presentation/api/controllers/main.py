from fastapi import FastAPI
from src.presentation.api.controllers.voice_controller import voice_router


def setup_controllers(app: FastAPI):
    app.include_router(voice_router)
