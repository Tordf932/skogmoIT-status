#!/usr/bin/env python3
import os, codecs, itscreen
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.1.232'  # IP Address of Raspberry Pi
host_port = 80

class MyServer(BaseHTTPRequestHandler):

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'iso-8859-1'))
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("iso-8859-1")
        post_data = post_data.split("=")[1]

        if post_data == 'ledig':
            itscreen.ledig()
        if post_data == 'mote':
            itscreen.mote()
        if post_data == 'annet':
            itscreen.annet_oppdrag()
        else:
            itscreen.pygame.display.update()

        print("Status: {}".format(post_data))
        
        self._redirect('/')  # Redirect back to the root url
        
http_server = HTTPServer((host_name, host_port), MyServer)

def webstart():
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()

def webstop():
    print("Server Stops - %s:%s" % (host_name, host_port))

    try:
        http_server.server_close()
    except KeyboardInterrupt:
        http_server.server_close()
