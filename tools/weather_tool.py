import openmeteo_requests
import requests_cache
from retry_requests import retry

# Setup Open-Meteo client with cache & retry
cache_session = requests_cache.CachedSession(
    ".cache", expire_after=3600
)
retry_session = retry(
    cache_session, retries=3, backoff_factor=0.2
)

openmeteo = openmeteo_requests.Client(session=retry_session)

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"

def get_weather(city: str):
    # Step 1: Geocoding (city -> lat/lon)
    geo_response = retry_session.get(
        GEOCODE_URL,
        params={"name": city, "count": 1},
        timeout=10
    )
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    if "results" not in geo_data:
        raise ValueError(f"City not found: {city}")

    location = geo_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]

    # Step 2: Fetch current weather
    responses = openmeteo.weather_api(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
    )

    response = responses[0]
    current = response.Current()

    return {
        "city": city,
        "temperature_c": current.Variables(0).Value(),
        "windspeed_kmh": current.Variables(1).Value(),
        "latitude": latitude,
        "longitude": longitude
    }