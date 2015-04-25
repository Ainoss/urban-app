#pip install TwitterAPI

from TwitterAPI import TwitterAPI

def start_getting_tweets():
	consumer_key = "KCZCsNS4OKwguAnnlZWUXXgI4"
	consumer_secret = "AfNy0WptjYQII5nb5DOSUEYSZvfoQnZc8nQXt4HmrUx5PwL9cP"
	access_token_key = "3204574607-Pu29CZKs2uo7VE50pOjI0A12w2v12MtZSGIYoro"
	access_token_secret = "0czZF7E6IopZQF3OBAKkKUdRWCKUhT2XBLVD7NHxcxlV6"
	file_name = "test"
	f = open("test", "a")
	api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
	
	r = api.request('statuses/filter', {'locations':'35,53,38,56'})
	for item in r.get_iterator():
		if 'text' in item:
			print "-------"
			print item['text']
		if 'coordinates' in item:
			if item['coordinates']:
				print "asda:"
				print item['coordinates']['coordinates'][0]
				print "asfaf: "
				print item['coordinates']['coordinates'][1]
			else:
				print "bla-bla"
		f.write(str(item).encode('utf-8'))
	


if __name__ == '__main__':
	start_getting_tweets()
