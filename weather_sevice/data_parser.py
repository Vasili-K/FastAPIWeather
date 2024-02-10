from weather_sevice.exceptions import InvalidWeatherDataSetError


def parse_weather_data(weather_json):
    try:
        weather_city = weather_json["name"]
        weather_country = weather_json["sys"]["country"]
        weather = weather_json["weather"][0]["main"]
        weather_description = weather_json["weather"][0]["description"]
        temperature = round(weather_json["main"]["temp"] - 273.15)
        feels_like = round(weather_json["main"]["feels_like"] - 273.15)
        wind = weather_json["wind"]["speed"]
        result = {
            'city': weather_city,
            'country': weather_country,
            'weather': weather,
            'description': weather_description,
            'temperature': temperature,
            'feels_like': feels_like,
            'wind': wind
        }
    except KeyError:
        raise InvalidWeatherDataSetError("Impossible to parse weather data.")
    return result
