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

from record import *
from decision import *
from test_get_tweets import *
from pars_photo import *
from time import time
import threading


data_to_send = "Valera"

array = []
array.append({
"longitude":"37.6",
"latitude":"55.7",
"messages":["Valera1","vlera2","ds","ssddddddddddddddd"],
"size":6
})

data_to_send = {"data": array}
data_to_send = json.dumps( data_to_send )
data_to_send = data_to_send + ' \n'
data_to_send = data_to_send.replace('[','\n[')
http_header = 'HTTP/1.1 200 OK \n ate: Mon, 23 May 2005 22:38:34 GMT \nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux) \nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT \nETag: "3f80f-1b6-3e1cb03b" \nContent-Type: text/html; charset=UTF-8 \nContent-Length: 138 \nAccept-Ranges: bytes\nConnection: close\n'


class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True


class EchoRequestHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        return SocketServer.BaseRequestHandler.setup(self)

    def handle(self):
        data = self.request.recv(1024)
        self.request.send(bytes(data_to_send))
        return

    def finish(self):
        return SocketServer.BaseRequestHandler.finish(self)


server = MyTCPServer(('0.0.0.0', 80), EchoRequestHandler)
#server = MyTCPServer(('10.80.7.23', 80), SimpleHTTPRequestHandler)
t1 = Thread(target=start_getting_tweets, args=())
t2 = Thread(target=start_getting_photos, args=())
t1.start()
t2.start()
server.serve_forever()
