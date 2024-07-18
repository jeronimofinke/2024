import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.1734,
	"longitude": 7.52781,
	"hourly": ["temperature_2m", "precipitation_probability", "rain", "weather_code", "visibility"],
	"timezone": "Europe/Berlin",
	"past_days": 2,
	"forecast_days": 1
}
responses = openmeteo.weather_api(url, params=params)

# Process first locationls
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_precipitation_probability = hourly.Variables(1).ValuesAsNumpy()
hourly_rain = hourly.Variables(2).ValuesAsNumpy()
hourly_weather_code = hourly.Variables(3).ValuesAsNumpy()
hourly_visibility = hourly.Variables(4).ValuesAsNumpy()

hourly_data = {"     Datum             Uhrzeit": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["Temperatur in Emsdetten"] = hourly_temperature_2m
hourly_data["Niederschlag %"] = hourly_precipitation_probability
pd.set_option("display.max_rows", None)
hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)