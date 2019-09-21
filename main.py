from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


API_KEY = '5ae74e1d6e23754d0228218b7ecfa1be'

# Synchronous way
darksky = DarkSky(API_KEY)

latitude = 42.3601
longitude = -71.0589
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

print(forecast.currently.temperature)

