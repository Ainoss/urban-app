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
        self.request.send(bytes(get_data_to_send()))
        return

    def finish(self):
        return SocketServer.BaseRequestHandler.finish(self)


server = MyTCPServer(('0.0.0.0', 80), EchoRequestHandler)
#server = MyTCPServer(('10.80.7.23', 80), SimpleHTTPRequestHandler)
try:
    t1 = Thread(target=start_getting_tweets, args=())
    t2 = Thread(target=start_getting_photos, args=())
except:
    print 'Init of server or threads problem'
else:
    t1.start()
    t2.start()
    server.serve_forever()


