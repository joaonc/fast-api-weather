from typing import Optional

import fastapi
from fastapi import Depends
from fastapi_cache.decorator import cache

from app.models.location import Location
from app.services import openweather_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
@cache(expire=10)
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report(loc.city, loc.state, loc.country, units)
    except Exception as e:
        return fastapi.responses.JSONResponse(str(e), status_code=400)
