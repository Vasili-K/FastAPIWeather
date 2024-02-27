from fastapi import FastAPI

from middleware.class_based_middlewear import CustomLoggingMiddlewareClass
from middleware.function_based_middlewear import add_process_time_header
from weather_service.weather_endpoints import weather_router

# main point of interaction to create API
app = FastAPI()


# add function based middleware
app.middleware('http')(add_process_time_header)

# add class based middleware
app.add_middleware(CustomLoggingMiddlewareClass)

app.include_router(weather_router, prefix="/api/v1", tags=["Weather Endpoint"])

