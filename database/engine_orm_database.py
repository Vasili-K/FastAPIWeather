from sqlalchemy.ext.asyncio import create_async_engine

from env_variables import USER_NAME, POSTGRES_PASSWORD

DATABASE_URL = f"postgresql+asyncpg://{USER_NAME}:{POSTGRES_PASSWORD}@localhost/weather_db"
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
