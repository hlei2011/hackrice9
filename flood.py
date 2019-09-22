from geopy.distance import great_circle
import requests
from pandas import DataFrame as df
import pandas
<<<<<<< HEAD
import plotly.graph_objects as go 

floods = pandas.read_csv('')

fig = go.Figure(go.Densitymapbox(lat=floods.Latitude, lon = floods.Longitude))
fig.update_layout(mapbox_style = "x", mapbox_center_lon = 180)
fig.update_layout(margin = {"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

=======
>>>>>>> ec002a2c0950c3c66b7c4c7d76beb880de0d03a4
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

ad1 = get_lat_lng('AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs', input("enter address: "))
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

def frange(x, y, jump):
      while x < y:
        yield x
        x += jump

#25511 Merrimac Trace Ct
output = get_elevation('AIzaSyCvQdjt2eydgLImEXQYnNHkz98fIVOQWhs')
print(output)

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
