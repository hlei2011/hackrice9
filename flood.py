from geopy.distance import great_circle
import requests
from pandas import DataFrame as df

"""
ad1 = input("enter address").replace(" ", "+")
response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+ad1)
print(response)
print(response.ur)
resp_json_payload = response.json()
print(resp_json_payload['results'][0]['geometry']['location'])
"""

def get_lat_lng(apiKey, address):
    """
    Returns the latitude and longitude of a location using the Google Maps Geocoding API. 
    API: https://developers.google.com/maps/documentation/geocoding/start

    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    address                 [str]

    # RETURN ------------------------------------------------------------------
    lat                     [float] 
    lng                     [float] 
    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        #print(resp_json_payload)
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        #print(e)
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat, lng

print(get_lat_lng('AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs', input("enter address: ")))


# name, lat, lng, class, flowinfo, url

v = open("mv01d_h12.txt")



great_circle()
