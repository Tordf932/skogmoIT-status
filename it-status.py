#!/usr/bin/env python3

import os, pygame, codecs
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '10.0.2.15'  # IP Address of Raspberry Pi
host_port = 8000

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

screen.fill(white)
pygame.display.update()


class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        html = '''
           <html>
            <head>
                <title>IT-DØR</title>
            </head>
           <body
            style="width:960px; margin: 20px auto;">
           <h1>IT-KONTOR STATUS</h1>
           <form action="/" method="POST">
               Status:
               <input type="submit" name="submit" value="LEDIG">
               <input type="submit" name="submit" value="MØTE">
               <input type="submit" name="submit" value="ANNET OPPDRAG">
           </form>
           </body>
           </html>
        '''
        self.do_HEAD()
        self.wfile.write(html.format().encode("iso-8859-1"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("iso-8859-1")
        post_data = post_data.split("=")[1]

        if post_data == 'LEDIG':
            ledig()
        if post_data == 'MØTE':
            mote()
        if post_data == 'ANNET OPPDRAG':
            annet_oppdrag()
        else:
            pygame.display.update()

        print("Status: {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url

def ledig():
    screen.fill(red)
    pygame.display.update()

def mote():
    screen.fill(red)
    pygame.display.update()

def annet_oppdrag():
    screen.fill(red)
    pygame.display.update()

# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
