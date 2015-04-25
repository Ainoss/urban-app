from Queue import Queue 

class Record:
    def __init__(self, x, y, m):
        self.latitude = x
        self.longitude = y
        self.message = m

records = Queue()


def set_record(latitude, longitude, message):
    records.put(Record(latitude, longitude, message))

def get_record():
    return records.get()

def delete_records_older_then_sec():

def is_empty():
    return records.empty()



