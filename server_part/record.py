from time import time 

class Record:
    latitude = 0.0
    longitude = 0.0
    message = ""
    time = 0.0

records = []

def set_record(record):
    records.append(record)

def get_records():
    return records

def ramove_old_records():
    if ( len(records) == 0 ):
        return
    old_time = 3600
    num = 0
    curr_time = time()
    while curr_time - records[num].time > old_time:
        num += 1
    records = records[num:]




