from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.presentation.api.controllers.main import setup_controllers
from src.presentation.api.providers.main import setup_providers
from src.presentation.api.middlewares.main import setup_middlewares


def init_api():
    app = FastAPI(debug=False, title="bpmn_backend_service", version="1.0.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    setup_controllers(app)
    setup_providers(app)
    setup_middlewares(app)

    return app


async def run_api():
    app = init_api()
    config = uvicorn.Config(app, host="localhost", port=8000)
    server = uvicorn.Server(config)

    await server.serve()
