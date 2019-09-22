import numpy
import math
import pandas
from geopy.distance import great_circle
import csv

resv_df = pandas.read_csv("mv01d_h12.txt")
resv_df.head()
resv_matrix = resv_df.iloc[:, :].values

prec_df = pandas.read_csv("precip-data.txt")
prec_df.head()
prec_matrix = prec_df.iloc[:, :].values
precip = {}
for i in prec_matrix:
    first = float(i[0])
    second = float(i[1])
    precip[(round(first*100)/100.0, round(second*100)/100.0)] = i[2]



def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


def prox(lat, long):
    
    mv = 9999999999
    for i in frange(29.7, 31.7, .05):
        for g in frange(-98, -94, .05):
            for f in resv_matrix:
                dis = great_circle((i, g), (f[1], f[2]))
                if (dis < mv):
                    mv = dis
    return mv


flood_df = pandas.read_csv("FilteredInstruments.csv")
flood_df.head()
flood_matrix = flood_df.iloc[:, :].values

elev_df = pandas.read_csv("elevation-data.txt")
elev_df.head()
elev_matrix = elev_df.iloc[:, :].values
elev_dict = {}

for i in elev_matrix:
    first = float(i[0])
    second = float(i[1])
    elev_dict[(round(first*100)/100.0, round(second*100)/100.0)] = i[2]

relevant = []
for i in flood_matrix:
    if i[10] > 29.7 and i[10] < 31.7 and i[11] < -94 and i[11] > -98:
        relevant.append(i)


def distance(lat, long, mtx):
    mini = 999999999
    for i in mtx:
        dis = math.sqrt((i[10] - lat) ** 2 + (i[11] - long) ** 2)
        if dis < mini:
            mini = dis
    return mini


class Location:
    def __init__(self, latitude, longitude, precipitation, elevation):
        self._latitude = latitude
        self._longitude = longitude
        self._precipitation = precipitation
        self._elevation = elevation
        #self._proximity = proximity

    def get_coords(self):
        return (self._latitude, self._longitude)

    def get_lat(self):
        return self._latitude

    def get_long(self):
        return self._longitude

    def get_list(self):
        return [self._precipitation, self._elevation]

    def get_flood_number(self):
        return 1 / (distance(self._latitude, self._longitude, relevant)) ** 2


locations = []

for i in frange(29.7, 31.7, 0.05):
    for j in frange(-98.0, -94.0, 0.05):
        k = round(i*100)/100.0
        l = round(j*100)/100.0
        print(k,l)
        locations.append(Location(k, l, precip[(k, l)], elev_dict[(k, l)]))


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

    xtx = numpy.matmul(numpy.transpose(input_data), input_data)
    xtx_inv = numpy.linalg.inv(xtx)
    ytx = numpy.matmul(numpy.transpose(output_data), input_data)

    return LinearModel(numpy.transpose(numpy.matmul(ytx, xtx_inv)))


inp = []
output = []
loc = []
test = []
testloc = []
for i in locations:
    print(i)
    if i.get_lat() > 30 or i.get_long() < -95.6 or i.get_long() > -95.2:
        inp.append(i.get_list())
        output.append([i.get_flood_number()])
        loc.append(i.get_coords())
    else:
        test.append(i.get_list())
        testloc.append(i.get_coords())

print(inp)
print(output)
lin = fit_least_squares(inp, output)
print(lin.get_weights())
floodtrain = list(numpy.matmul(inp, lin.get_weights()))
floodtest = list(numpy.matmul(test, lin.get_weights()))
print(floodtrain)
print(floodtest)
exp1 = []
exp2 = []
exp3 = []
for i in range(len(floodtest)):
    exp1.append(testloc[i][0])
    exp2.append(testloc[i][1])
    exp3.append(floodtest[i])
for i in range(len(floodtrain)):
    exp1.append(loc[i][0])
    exp2.append(loc[i][1])
    exp3.append(floodtrain[i])
#print(exp)
a = numpy.asarray(exp1)
b = numpy.asarray(exp2)
c = numpy.asarray(exp3)
numpy.savetxt("export1.csv", a)
numpy.savetxt("export2.csv", b)
numpy.savetxt("export3.csv", c)