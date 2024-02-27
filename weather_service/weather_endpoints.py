from fastapi import APIRouter

from models.weather_models import WeatherResponse
from weather_service.save_to_db import save_weather
from weather_service.weather_request import request_weather


weather_router = APIRouter()


@weather_router.get("/")
async def root():
    return {"message": "Hello From Weather Application"}


@weather_router.get("/weather")
async def get_weather(city: str, save: bool = True) -> WeatherResponse | str:
    result = await request_weather(city)
    try:
        weather_description = WeatherResponse(**result)
    except Exception:
        return "Probably you asked for something unexpected. Try another request."

    if save:
        await save_weather(weather_description)

    return weather_description