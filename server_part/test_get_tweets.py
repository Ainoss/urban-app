#pip install TwitterAPI

from TwitterAPI import TwitterAPI
from record import *
from decision import *
from time import time

data_to_send = ""


def start_getting_tweets():
    consumer_key = "KCZCsNS4OKwguAnnlZWUXXgI4"
    consumer_secret = "AfNy0WptjYQII5nb5DOSUEYSZvfoQnZc8nQXt4HmrUx5PwL9cP"
    access_token_key = "3204574607-Pu29CZKs2uo7VE50pOjI0A12w2v12MtZSGIYoro"
    access_token_secret = "0czZF7E6IopZQF3OBAKkKUdRWCKUhT2XBLVD7NHxcxlV6"
    file_name = "MyRecords"
    f = open(file_name, "a", 0)
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    r = api.request('statuses/filter', {'locations':'37.3,55.5,37.9,55.9'})
    n = 0
    for item in r.get_iterator():
        array = make_decision()
        temp = {"data": array}
        temp = json.dumps( data_to_send ) + ' \n'
        data_to_send = temp.replace(' ', '\n')
        print data_to_send
        print
        #if 'text' in item:
            #print "-------"
            #print item['text']
        if 'coordinates' in item:
            if item['coordinates']:
                #print item['coordinates']['coordinates'][0]
                #print item['coordinates']['coordinates'][1]
                record = Record()
                record.latitude = item['coordinates']['coordinates'][1]
                record.longitude = item['coordinates']['coordinates'][0]
                record.message = item['text']
                record.time = time();
                set_record(record)
                n += 1
                #f.write('n = ' + str(n) + '\n')
                #f.write(str(item['text'].encode('utf-8')) + '\n')
                #f.write(str(item['coordinates']['coordinates'][0]) + ' ')
                #f.write(str(item['coordinates']['coordinates'][1]) + '\n')
                #f.write(str(time()) + '\n')
                #f.write('\n')
                #have to be in another thread



#if __name__ == '__main__':
#    start_getting_tweets()
