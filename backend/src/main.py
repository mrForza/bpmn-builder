import asyncio
from src.presentation.api.main import run_api, init_api

app = init_api()

if __name__ == '__main__':
    asyncio.run(run_api())
