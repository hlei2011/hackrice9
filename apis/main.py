from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


API_KEY = '5ae74e1d6e23754d0228218b7ecfa1be'

# Synchronous way
darksky = DarkSky(API_KEY)


"""
    get a range of daily precipitation data points for a range of latitude and longitudes.
"""
latitude = 42.3601
longitude = -71.0589
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

def frange(x, y, jump):
      while x < y:
        yield x
        x += jump


a = ""

for i in frange(29.7, 31.7, 0.05):
    for g in frange(-98, -94, 0.05):
        forecast = darksky.get_forecast(
            i, g,
            extend=False, # default `False`
            lang=languages.ENGLISH, # default `ENGLISH`
            units=units.AUTO, # default `auto`
            exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
        )

        a += ""+str(i)+", "+str(g)+", "+str(forecast.daily.data[0].precip_intensity)+"\n"

print(a)