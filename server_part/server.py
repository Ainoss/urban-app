#SERVER PART OF THE PROGRAMM. pRESENTS PGABBED INFO IN JSON FORMAT

import SocketServer
import json

data_to_send = '{  "images" : [    {      "idiom" : "iphone",      "size" : "29x29",      "scale" : "2x"    },    {      "idiom" : "iphone",      "size" : "29x29",      "scale" : "3x"    },    {      "idiom" : "iphone",      "size" : "40x40",      "scale" : "2x"    },    {      "idiom" : "iphone",      "size" : "40x40",      "scale" : "3x"    },    {      "idiom" : "iphone",      "size" : "60x60",      "scale" : "2x"    },    {      "idiom" : "iphone",      "size" : "60x60",      "scale" : "3x"    },    {      "idiom" : "ipad",      "size" : "29x29",      "scale" : "1x"    },    {      "idiom" : "ipad",      "size" : "29x29",      "scale" : "2x"    },    {      "idiom" : "ipad",      "size" : "40x40",      "scale" : "1x"    },    {      "idiom" : "ipad",      "size" : "40x40",      "scale" : "2x"    },    {      "idiom" : "ipad",      "size" : "76x76",      "scale" : "1x"    },    {      "idiom" : "ipad",      "size" : "76x76",      "scale" : "2x"    }  ],  "info" : {    "version" : 1,    "author" : "xcode"  }}'

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = json.loads(self.request.recv(1024).strip())
            # process the data, i.e. print it:
            print data
            # send some 'ok' back
            self.request.sendall(json.dumps({'return':'ok'}))
        except Exception, e:
            print "Exception wile receiving message: ", e



class EchoRequestHandler(SocketServer.BaseRequestHandler):
    
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        return SocketServer.BaseRequestHandler.setup(self)

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        self.request.send(data_to_send)
        return

    def finish(self):
        return SocketServer.BaseRequestHandler.finish(self)


server = MyTCPServer(('127.0.0.1', 80), EchoRequestHandler)
server.serve_forever()