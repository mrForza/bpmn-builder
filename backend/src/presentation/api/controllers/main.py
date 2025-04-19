from fastapi import FastAPI
from presentation.api.controllers.voice_controller import voice_router


def setup_controllers(app: FastAPI):
    app.include_router(voice_router)