from fastapi import FastAPI
from presentation.api.controllers.main import setup_controllers
from presentation.api.providers.main import setup_providers
from presentation.api.middlewares.main import setup_middlewares


def init_api():
    app = FastAPI(debug=False, title="bpmn_backend_service", version="1.0.0")

    setup_controllers(app)
    setup_providers(app)
    setup_middlewares(app)
    
    return app


async def run_api():
    pass
