#SERVER PART OF THE PROGRAMM. pRESENTS PGABBED INFO IN JSON FORMAT

__version__ = "0.6"

__all__ = ["SimpleHTTPRequestHandler"]

import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import shutil
import mimetypes
from StringIO import StringIO
import SocketServer
import json
from threading import Thread
import time

from TwitterAPI import TwitterAPI
from record import *
from decision import *
from time import time
import threading


data_to_send = "Valera"

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
        array = make_decision()
        print array
        temp = {"data": array}
        temp = json.dumps( temp ) + ' \n'
        global data_to_send
        data_to_send = temp
        print data_to_send
        print
        #dummy_event = threading.Event()
        #dummy_event.wait(timeout=1)
                #f.write('n = ' + str(n) + '\n')
                #f.write(str(item['text'].encode('utf-8')) + '\n')
                #f.write(str(item['coordinates']['coordinates'][0]) + ' ')
                #f.write(str(item['coordinates']['coordinates'][1]) + '\n')
                #f.write(str(time()) + '\n')
                #f.write('\n')
                #have to be in another thread


class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True


class EchoRequestHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        print "Connection oppening"
        return SocketServer.BaseRequestHandler.setup(self)

    def handle(self):
        data = self.request.recv(1024)
        print "Handling"
        print data
        self.request.sendall(data_to_send)
        print "Sending data!"
        return

    def finish(self):
        print "Connection closing"
        print ""
        print ""
        return SocketServer.BaseRequestHandler.finish(self)


server = MyTCPServer(('10.80.7.23', 80), EchoRequestHandler)
#server = MyTCPServer(('10.80.7.23', 80), SimpleHTTPRequestHandler)
t = Thread(target=start_getting_tweets,args=() )
t.start()
server.serve_forever()
