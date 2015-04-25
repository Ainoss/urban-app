#pip install TwitterAPI

from TwitterAPI import TwitterAPI
from record import *
from decision import *

def start_getting_tweets():
    consumer_key = "KCZCsNS4OKwguAnnlZWUXXgI4"
    consumer_secret = "AfNy0WptjYQII5nb5DOSUEYSZvfoQnZc8nQXt4HmrUx5PwL9cP"
    access_token_key = "3204574607-Pu29CZKs2uo7VE50pOjI0A12w2v12MtZSGIYoro"
    access_token_secret = "0czZF7E6IopZQF3OBAKkKUdRWCKUhT2XBLVD7NHxcxlV6"
    file_name = "MyRecords"
    f = open(file_name, "a")
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    r = api.request('statuses/filter', {'locations':'37.3,55.5,37.9,55.9'})
    num = 0
    print 'START'
    for item in r.get_iterator():
        print "-------"
        if 'text' in item:
            print item['text']
        if 'coordinates' in item:
            if item['coordinates']:
                print item['coordinates']['coordinates'][0]
                print item['coordinates']['coordinates'][1]
                set_record(item['coordinates']['coordinates'][1], item['coordinates']['coordinates'][0], item['text'])
                make_decision()
        num += 1
        f.write('n = ' + str(num))
        f.write(str(item).encode('utf-8'))
        f.write('\n\n')



if __name__ == '__main__':
    start_getting_tweets()
