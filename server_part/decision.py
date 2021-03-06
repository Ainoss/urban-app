from record import *
from math import floor

# from 0 to 180
max_long = 37.9
min_long = 37.3
# from -90 to 90
max_lat = 55.9
min_lat = 55.5

grid_lat_size = 14
grid_long_size = 14
step_lat = (max_lat - min_lat) / float(grid_lat_size)
step_long = (max_long - min_long) / float(grid_long_size)


def make_decision(  ):
    twits = get_records()
    map_data = [[[] for x in range(grid_lat_size)] for x in range(grid_long_size)]
    weight_data = [[0.0 for x in range(grid_lat_size)] for x in range(grid_long_size)]
    max_weight = 0.0
    for twit in twits:
        x = twit.latitude
        y = twit.longitude
        if min_lat <= x and x <= max_lat and min_long <= y and y <= max_long:
            i = int(floor((x - min_lat) / step_lat))
            j = int(floor((y - min_long) / step_long))
            map_data[i][j].append(twit)
            weight_data[i][j] += twit.weight
            max_weight = max(max_weight, weight_data[i][j])
            print max_weight
            
    array_of_interesting_places = []
    for x in range(0,grid_lat_size):
        for y in range(0,grid_long_size):
            if weight_data[x][y] > max_weight * 0.5:
                interesting_place = {}
                lat_long = get_average_lat_long(map_data[x][y])
                interesting_place["latitude"] = str(lat_long["latitude"])
                interesting_place["longitude"] = str(lat_long["longitude"])
                interesting_place["messages"] = []
                interesting_place["size"] = len(map_data[x][y])
                for twit in map_data[x][y]:
                    if len(twit.message) > 0:
                        try:
                            interesting_place["messages"].append( twit.message.encode('utf-8') )
                        except:
                            interesting_place["messages"].append( twit.message )
                interesting_place["messages"].append("")
                array_of_interesting_places.append(interesting_place)
    #remove_old_records()
    return array_of_interesting_places

def get_average_lat_long( twits ):
    avg_lat_long = { "latitude" : 0.0, "longitude" : 0.0  }
    for twit in twits:
        avg_lat_long["latitude"] = avg_lat_long["latitude"] + float(twit.latitude)
        avg_lat_long["longitude"] = avg_lat_long["longitude"] + float(twit.longitude)
    avg_lat_long["latitude"] = avg_lat_long["latitude"] / (len(twits))
    avg_lat_long["longitude"] = avg_lat_long["longitude"] / (len(twits))
    return avg_lat_long
