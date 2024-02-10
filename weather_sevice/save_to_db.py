from sqlalchemy.ext.asyncio import AsyncSession

from database.engine_orm_database import engine
from database.wheather_tables import Weather


async def save_weather(weather_description):
    async with AsyncSession(engine) as session:
        async with session.begin():
            weather = Weather(**weather_description.dict())
            session.add(weather)
