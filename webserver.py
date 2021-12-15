#!/usr/bin/env python3
import os, codecs, itscreen
from bs4 import BeautifulSoup as bs
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
                self.wfile.write(bytes(f, "iso-8859-1"))
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
        soup = bs(open("index.html"), "html.parser")
        if post_data == 'btn1':
            search =soup.find('button', class_='button_ledig')
            if search != None:
                search['class'] = 'button_ledig_active'
            search2 =soup.find('button', class_='button_mote_active')
            if search2 != None:
                search2['class'] = 'button_mote'
            search3 =soup.find('button', class_='button_annet_active')
            if search3 != None:
                search3['class'] = 'button_annet'
            with open("index.html", "w") as outf:
                outf.write(str(soup))
            itscreen.ledig()
        if post_data == 'btn2':
            search =soup.find('button', class_='button_ledig_active')
            if search != None:
                search['class'] = 'button_ledig'
            search2 =soup.find('button', class_='button_mote')
            if search2 != None:
                search2['class'] = 'button_mote_active'
            search3 =soup.find('button', class_='button_annet_active')
            if search3 != None:
                search3['class'] = 'button_annet'
            with open("index.html", "w") as outf:
                outf.write(str(soup))
            itscreen.mote()
        if post_data == 'btn3':
            search =soup.find('button', class_='button_ledig_active')
            if search != None:
                search['class'] = 'button_ledig'
            search2 =soup.find('button', class_='button_mote_active')
            if search2 != None:
                search2['class'] = 'button_mote'
            search3 =soup.find('button', class_='button_annet')
            if search3 != None:
                search3['class'] = 'button_annet_active'
            with open("index.html", "w") as outf:
                outf.write(str(soup))
            itscreen.annet_oppdrag()
        else:
            print("could not post")

        print("Status: {}".format(post_data))
        
        self._redirect('/')  # Redirect back to the root url

http_server = HTTPServer((host_name, host_port), MyServer)

def webstart():
    print("Server Starts - %s:%s" % (host_name, host_port))
    soup = bs(open("index.html"), "html.parser")
    first_start = True
    if first_start:
        search =soup.find('button', class_='button_ledig_active')
        if search != None:
            search['class'] = 'button_ledig'
        search2 =soup.find('button', class_='button_mote_active')
        if search2 != None:
            search2['class'] = 'button_mote'
        search3 =soup.find('button', class_='button_annet_active')
        if search3 != None:
            search3['class'] = 'button_annet'
        with open("index.html", "w") as outf:
            outf.write(str(soup))
        first_start = False
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
