#pip install TwitterAPI

from TwitterAPI import TwitterAPI
from record import *
from decision import *
from time import time
import json

data_to_send = "Init"

def get_data_to_send():
    global data_to_sand
    return data_to_send

def start_getting_tweets():
    consumer_key = "KCZCsNS4OKwguAnnlZWUXXgI4"
    consumer_secret = "AfNy0WptjYQII5nb5DOSUEYSZvfoQnZc8nQXt4HmrUx5PwL9cP"
    access_token_key = "3204574607-Pu29CZKs2uo7VE50pOjI0A12w2v12MtZSGIYoro"
    access_token_secret = "0czZF7E6IopZQF3OBAKkKUdRWCKUhT2XBLVD7NHxcxlV6"
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    r = api.request('statuses/filter', {'locations':'37.3,55.5,37.9,55.9'})
    for item in r.get_iterator():
        print "TWEET"
        if 'coordinates' in item:
            if item['coordinates']:
                record = Record()
                record.latitude = item['coordinates']['coordinates'][1]
                record.longitude = item['coordinates']['coordinates'][0]
                record.message = item['text']
                record.time = time();
                set_record(record)
        array = make_decision()
        tmp = {"data": array}
        tmp = json.dumps(tmp) + '\n'
        tmp = '{"data":\n' + tmp[ len('{"data":\n') :]
        global data_to_send
        data_to_send = tmp

#if __name__ == '__main__':
#    start_getting_tweets()

