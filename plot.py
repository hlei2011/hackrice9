import pandas as pd
import datetime
import numpy as np
#import plotly.plotly as py
#import plotly.plotly as py
import chart_studio as cs
import plotly.graph_objs as go

inp = pd.read_csv("export1.csv")
print(inp)
#inp = pd.DataFrame(inp, columns=['Latitude', 'Longitude', 'Magnitude'])

#print(inp)

#py.sign_in(username='guy477', api_key='pqkfBtB0LaoAmsS07Wd6')
cs.tools.set_credentials_file(username='guy477', api_key='pqkfBtB0LaoAmsS07Wd6')
cs.tools.set_config_file(world_readable=True, sharing='public')

fig = go.Figure(go.Densitymapbox(lat=inp.Latitude, lon=inp.Longitude, z=inp.Flood, radius=20))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=-95.7, mapbox_center_lat=30.62, mapbox_zoom=7.5)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


layout = go.Layout(
    title='Flood Heatmap (Higher Value = safer)')

fig = go.Figure(data=fig, layout=layout)

cs.plotly.plot(fig, filename='Flood Heat Map (Higher Value = Safer)')

