import json

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from services import openweather_service
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_api_keys():
    with open('settings.json') as f:
        settings = json.load(f)
        openweather_service.api_key = settings.get('api_key')


if __name__ == '__main__':
    configure()
    uvicorn.run(api)
else:
    # Run via asgi (unicorn)
    configure()