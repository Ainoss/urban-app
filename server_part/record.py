from time import time 

class Record:
    def __init__(self, x, y, m, t):
        self.latitude = x
        self.longitude = y
        self.message = m
        self.time = t

records = []

def set_record(latitude, longitude, message, time):
    records.append(Record(latitude, longitude, message, time))

def get_records():
    return records

def ramove_old_records():
    old_time = 300
    num = 0
    curr_time = time()
    while curr_time - records[num].time > old_time:
        num += 1
    records = records[num:]




