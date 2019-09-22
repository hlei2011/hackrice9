from geopy.distance import great_circle
import requests
from pandas import DataFrame as df
import pandas
import plotly.graph_objects as go 

floods = pandas.read_csv('')

fig = go.Figure(go.Densitymapbox(lat=floods.Latitude, lon = floods.Longitude))
fig.update_layout(mapbox_style = "x", mapbox_center_lon = 180)
fig.update_layout(margin = {"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

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

flood_df = pandas.read_csv("mv01d_h12.txt")
flood_df.head()
flood_matrix = flood_df.iloc[:,:].values

for i in range(len(flood_matrix)):
    address = flood_matrix[i][0] + flood_matrix[i][1]
    flood_matrix[i].pop(0)
    flood_matrix[i].pop(0)
    flood_matrix[i].insert(0, address)
    


great_circle()
