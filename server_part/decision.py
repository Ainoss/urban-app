from record import *
from math import floor

# from 0 to 180
max_long = 37.9
min_long = 37.3
# from -90 to 90
max_lat = 55.9
min_lat = 55.5

grid_lat_size = 10
grid_long_size = 10
step_lat = (max_lat - min_lat) / float(grid_lat_size)
step_long = (max_long - min_long) / float(grid_long_size)


def make_decision(  ):
    twits = get_records()
    map_data = [[[] for x in range(grid_lat_size)] for x in range(grid_long_size)]
    for twit in twits:
        x = twit.latitude
        y = twit.longitude
        if min_lat <= x and x <= max_lat and min_long <= y and y <= max_long:
            i = int(floor((x - min_lat) / step_lat))
            j = int(floor((y - min_long) / step_long))
            map_data[i][j].append(rec)
            if (len(map_data[i][j]) > 2):
                print i, j, "interesting!"
            else:
                print i, j, "will be interesting soon.."
        else:
            print 'WRONG COORD'
    array_of_interesting_places = []
    for x in range(0,max_lat):
        for y in range(0,max_long):
            if ( len(map_data[x][y]) > 2):
                interesting_place = {}
                lat_long = get_average_lat_long(map_data[x,y])
                interesting_place["latitude"] = str(lat_long["latitude"])
                interesting_place["longitude"] = str(lat_long["longitude"])
                interesting_place["messages"] = []
                for twit in map_data[x][y]:
                    interesting_place["messages"].append(twit.text)
                array_of_interesting_places.append(interesting_place)
                print "New interesting place added!"
                print interesting_place["messages"]
            else:
                print "Place is not interesting"
    return array_of_interesting_places

def get_average_lat_long( twits ):
    avg_lat_long = { "latitude" : 0.0, "longitude" : 0.0  }
    for twit in twits:
        avg_lat_long["latitude"] = avg_lat_long["latitude"] + float(twit.latitude)
        avg_lat_long["longitude"] = avg_lat_long["longitude"] + float(twit.longitude)
    avg_lat_long["latitude"] = avg_lat_long["latitude"] / (len(twits))
    avg_lat_long["longitude"] = avg_lat_long["longitude"] / (len(twits))
    return avg_lat_long