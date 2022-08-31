import json

import fastapi
import uvicorn
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from starlette.staticfiles import StaticFiles

from app.api import weather_api
from app.services import openweather_service
from app.views import home

app = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_routing():
    app.mount('/assets/static', StaticFiles(directory='assets/static'), name='static')
    app.include_router(home.router)
    app.include_router(weather_api.router)


def configure_api_keys():
    with open('settings.json') as f:
        settings = json.load(f)
        openweather_service.api_key = settings.get('api_key')


@app.on_event('startup')
async def startup():
    FastAPICache.init(InMemoryBackend())


if __name__ == '__main__':
    configure()
    uvicorn.run(app)
else:
    # Run via asgi (uvicorn)
    configure()
