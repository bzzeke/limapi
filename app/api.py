#!/usr/bin/python3

from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import urllib

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.respond()

    def respond(self):

        path = urllib.parse.unquote(self.path).strip("/")
        path = path.split("/")
        method = path[0]
        if hasattr(self, method):
            del path[0]
            response = getattr(self, method)(path)
        else:
            response = b""
            self.send_response(404)
            self.end_headers()

        self.wfile.write(response)

    def dash(self, args):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

        with open(os.environ["DASH_FILE"]) as f:
            return f.read().encode("utf-8")

        return ""

    def charts(self, args):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

        with open(os.environ["CHARTS_FILE"]) as f:
            return f.read().encode("utf-8")

        return ""

def main():
    server_address = ("", int(os.environ["DASH_PORT"]))
    httpd = ThreadingHTTPServer(server_address, Server)
    print("[dash_parser] Starting...")
    httpd.serve_forever()
