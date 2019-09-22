from geopy.distance import great_circle
import requests
from pandas import DataFrame as df
import pandas
import plotly.graph_objects as go 
import requests

#floods = pandas.read_csv('')
"""
fig = go.Figure(go.Densitymapbox(lat=floods.Latitude, lon = floods.Longitude))
fig.update_layout(mapbox_style = "x", mapbox_center_lon = 180)
fig.update_layout(margin = {"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
"""

def get_precipIntensity(apiKey, lat, lon):
    """
    Returns the precipation data (inches of liquid water per hour) of a location using DarkSky API.
    API: https://darksky.net/dev/docs

    #Input --------------------------------------------------------------
    apiKey                  [str]
    lat                     [float]
    lon                     [float]
    timezone                [str]  ------ 'America/Chicago' ------ Central

    #Return --------------------------------------------------------------
    precip_ntensity   [float]
    """
    timezone = 'America/Chicago'
    url = ('https://api.darksky.net/forecast/{}/{},{},{}'.format("5ae74e1d6e23754d0228218b7ecfa1be", lat, lon, timezone)
           .format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        #print(resp_json_payload)
        precip_ntensity = resp_json_payload['currently']['precipIntensity']
    except:
        print('ERROR: {}'.format(address))
        precip_ntensity = 0
    return precip_ntensity
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
        #ele = resp_json_payload['results']


        url = ("https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&sensor=true&key={}").format(lat, lng, apiKey)
        resp = requests.get(url)
        resp_json = resp.json()
        print(resp_json)
        print(resp_json['results'][0]['elevation'])
    except:
        #print(e)
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return (lat, lng)

#ad1 = get_lat_lng('AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs', input("enter address: "))
                  #AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs

# name, lat, lng, class, flowinfo, url

v = open("mv01d_h12.txt")

flood_df = pandas.read_csv("mv01d_h12.txt")
print(flood_df.head())
flood_matrix = flood_df.iloc[:,:].values
"""
for i in range(len(flood_matrix)):
    address = str(flood_matrix[i][0]) + str(flood_matrix[i][1])
    flood_matrix[i].pop(0)
    flood_matrix[i].pop(0)
    flood_matrix[i].insert(0, address)
"""

def frange(x, y, jump):
      while x < y:
        yield x
        x += jump

def get_precip(apiKey):
    a = ""
    for i in frange(29.7, 31.7, 0.05):
        for g in frange(-98, -94, 0.05):
            url = ('https://api.darksky.net/forecast/{}/{},{},{}'.format("5ae74e1d6e23754d0228218b7ecfa1be", i, g, 'America/Chicago'))
            resp = requests.get(url)
            resp_json = resp.json()
            print(resp_json)
            a += ""+str(i)+", "+str(g)+", "+str(resp_json['currently']['precipIntensity'])+'\n'
    return a

output1 = get_precip("5ae74e1d6e23754d0228218b7ecfa1be")
print (output1)

def get_elevation(apiKey):
    a = ""
    for i in frange(29.7, 31.7, .05):
        for g in frange(-98, -94, .05):
            url = ("https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&sensor=true&key={}").format(i, g, apiKey)
            resp = requests.get(url)
            resp_json = resp.json()
            print(resp_json)
            a += ""+str(i)+", "+str(g)+", "+str(resp_json['results'][0]['elevation'])+'\n'
    return a


#25511 Merrimac Trace Ct
#output = get_elevation('AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs')
#print(output)

#print(flood_matrix[0][0])
m = ""
mv = 9999999999
for i in range(len(flood_matrix)):
    dis = great_circle(get_lat_lng('AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs', flood_matrix[i][0][14:]), ad1)
    if (great_circle(get_lat_lng('AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs', flood_matrix[i][0][14:]), ad1)<mv):
        m = flood_matrix[i][0]
        mv = dis
        print(m)
print(m)
