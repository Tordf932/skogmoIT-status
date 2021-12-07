#!/usr/bin/env python3

import os, pygame, codecs
from http.server import BaseHTTPRequestHandler, HTTPServer

pygame.init()
pygame.font.init()

host_name = '192.168.1.232'  # IP Address of Raspberry Pi
host_port = 80
sw = 1920
sh = 1080
screen = pygame.display.set_mode((sw, sh))#pygame.FULLSCREEN
clock = pygame.time.Clock()
bg = pygame.image.load("assets/bg.png")
font1 = pygame.font.SysFont("None", 200)
font2 = pygame.font.SysFont("None", 100)
font3 = pygame.font.SysFont("None", 50)

text_ledig = font1.render("LEDIG", False, (255,255,255))
text_rect1 = text_ledig.get_rect(center=(sw/2, sh/2))
text_ledig2 = font1.render("KOM INN!", False, (255,255,255))
text_rect12 = text_ledig2.get_rect(center=(sw/2, sh/1.6))

text_mote = font1.render("SITTER I MØTE", False, (255,255,255))
text_rect2 = text_mote.get_rect(center=(sw/2, sh/2))
text_mote2 = font2.render("KOM TILBAKE SENERE", False, (255,255,255))
text_rect22 = text_mote2.get_rect(center=(sw/2, sh/1.6))

text_annet = font1.render("VI HAR ANNET OPPDRAG", False, (255,255,255))
text_rect3 = text_annet.get_rect(center=(sw/2, sh/2))
text_annet2 = font3.render("RING: 35919209", False, (255,255,255))
text_rect32 = text_annet2.get_rect(center=(sw/2, sh/1.6))

white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

screen.fill(white)
pygame.display.update()


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
            ledig()
        if post_data == 'mote':
            mote()
        if post_data == 'annet':
            annet_oppdrag()
        else:
            pygame.display.update()

        print("Status: {}".format(post_data))
        
        self._redirect('/')  # Redirect back to the root url

def ledig():
    screen.blit(bg, (0,0))
    screen.blit(text_ledig, text_rect1)
    screen.blit(text_ledig2, text_rect12)
    pygame.display.update()

def mote():
    screen.blit(bg, (0,0))
    screen.blit(text_mote, text_rect2)
    screen.blit(text_mote2, text_rect22)
    pygame.display.update()

def annet_oppdrag():
    screen.blit(bg, (0,0))
    screen.blit(text_annet, text_rect3)
    screen.blit(text_annet2, text_rect32)
    pygame.display.update()

# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
