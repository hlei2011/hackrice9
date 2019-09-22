import numpy
import pandas

flood_df = pandas.read_csv("FilteredInstruments.csv")
flood_df.head()
flood_matrix = flood_df.iloc[:,:].values

relevant = []
for i in flood_matrix:
    if i[10] > 29.7 and i[10] < 31.7 and i[11] < -94 and i[11] > -98:
        relevant.append(i)
        
def distance (lat, long, mtx):
    mini = 5
    for i in mtx:
        dis = sqrt((i[10] - lat)**2 + (i[11] - long)**2)
        if dis < mini:
            mini = dis
    return mini

class Location:
    def __init__(self, latitude, longitude, precipitation, elevation, proximity, flood):
        self._latitude = latitude
        self._longitude = longitude
        self._precipitation = precipitation
        self._eleneoprvation = elevation
        self._proximity = proximity
        self._flood = flood
    
    def get_coords():
        return (self._latitude, self._longitude)
    
    def get_list():
        return [self._precipitation, self._elevation, self._proximity]
        
    def get_flood_number():
        return 1/(distance(self._latitude, self._longitude, relevant))**2
    
locations = []

                                                    
for i in range(29.7,31.7,0.05):
    for j in range(-98.0,-94.0,0.05):
        locations.append(Location(i, j, precip(i,j), elev(i,j), prox(i,j), flood(i,j)))




class LinearModel:
   
    def __init__(self, weights):
        self._weights = weights

    def __str__(self):
        return str(self._weights)

    def get_weights(self):
        return self._weights

    def generate_predictions(self, inputs):
        return numpy.matmul(inputs, self._weights)

def fit_least_squares(input_data, output_data):
    # This function's code follows the formula for finding the weights
    # that create the least mean-squared error, which is:
    #  w = (((y_t)x)(inv((x_t)x))_t)

    xtx = numpy.matmul(numpy.transpose(input_data),input_data)
    xtx_inv = numpy.linalg.inv(xtx)
    ytx = numpy.matmul(numpy.transpose(output_data),input_data)

    return LinearModel(numpy.transpose(numpy.matmul(ytx,xtx_inv)))
