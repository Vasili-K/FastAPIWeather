

class WeatherParseError(Exception):
    """Common error for weather data parsing"""


class InvalidWeatherDataSetError(WeatherParseError):
    """Error when not all data present in the weather json"""

