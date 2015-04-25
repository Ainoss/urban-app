import random
from math import floor
from record import get_record, is_empty, set_record

def fill_records():
    n = 1000
    while n > 0:
        n -= 1
        x = random.uniform(0, 10);
        y = random.uniform(0, 10);
        m = 'fij'
        set_record(x, y, m)
    

# from -90 to 90
max_lat = 10
min_lat = 0
# from 0 to 180
max_long = 10
min_long = 0

grid_lat_size = 10
grid_long_size = 10
step_lat = (max_lat - min_lat) / grid_lat_size
step_long = (max_long - min_long) / grid_long_size

map_data = [[[]] * grid_lat_size] * grid_long_size

fill_records()

while not is_empty():
    rec = get_record()
    x = rec.latitude
    y = rec.longitude
    i = int(floor((x - min_lat) / step_lat))
    j = int(floor((y - min_long) / step_long))
    map_data[i][j].append(rec)




