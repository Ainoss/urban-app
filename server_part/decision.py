from record import *
from math import floor

# from -90 to 90
max_lat = 38.0
min_lat = 35.0
# from 0 to 180
max_long = 56.0
min_long = 53.0

grid_lat_size = 10
grid_long_size = 10
step_lat = (max_lat - min_lat) / float(grid_lat_size)
step_long = (max_long - min_long) / float(grid_long_size)
    
map_data = [[[] for x in range(grid_lat_size)] for x in range(grid_long_size)]

def make_decision():
    while not is_empty():
        rec = get_record()
        x = rec.latitude
        y = rec.longitude
        i = int(floor((x - min_lat) / step_lat))
        j = int(floor((y - min_long) / step_long))
        map_data[i][j].append(rec)
        if (len(map_data[i][j]) > 2):
            print i, j, "interesting!"
        else:
            print i, j, "will be interesting soon.."


