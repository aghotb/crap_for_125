from urlparse import urlparse, parse_qs
import urllib2
from lxml.html import fromstring
import requests
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
def recommendations(location, condition):
    # do stuff
    if condition == "diiatbetes":
        sql.select(dibetes)
    
    return "Fetching restaruants in " + location + " for " + condition
    
class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("Starting GET")
        self._set_headers()
        # Or use the parse_qs method
        res = recommendations("irvine", "diabetes")
        self.wfile.write("<html><body><h1>" + res + "</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


run(port=8000)



