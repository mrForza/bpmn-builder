import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.routes.main import main_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(main_router)

if __name__ == "__main__":
    config = uvicorn.Config(app, host="localhost", port=8000)
    server = uvicorn.Server(config)

    asyncio.run(server.serve())
