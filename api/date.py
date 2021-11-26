from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        _date = {'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        self.wfile.write(json.dumps({'date': _date}).encode("utf-8"))