from geopy.distance import great_circle
import requests
from pandas import DataFrame as df
import pandas
import plotly.graph_objects as go 
import requests


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
    url = ('https://api.darksky.net/forecast/{}/{},{},{}'.format("darksky api key", lat, lon, timezone)
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


v = open("mv01d_h12.txt")

flood_df = pandas.read_csv("mv01d_h12.txt")
print(flood_df.head())
flood_matrix = flood_df.iloc[:,:].values

def frange(x, y, jump):
      while x < y:
        yield x
        x += jump

def get_precip(apiKey):
    a = ""
    for i in frange(29.7, 31.7, 0.05):
        for g in frange(-98, -94, 0.05):
            url = ('https://api.darksky.net/forecast/{}/{},{},{}'.format("darksky api key", i, g, 'America/Chicago'))
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


m = ""
mv = 9999999999
for i in range(len(flood_matrix)):
    dis = great_circle(get_lat_lng('google api key', flood_matrix[i][0][14:]), ad1)
    if (great_circle(get_lat_lng('google api key', flood_matrix[i][0][14:]), ad1)<mv):
        m = flood_matrix[i][0]
        mv = dis
        print(m)
print(m)
