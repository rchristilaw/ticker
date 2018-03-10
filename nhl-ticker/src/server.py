from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from ticker import Ticker

class TickerHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!" + self.server.test + "</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1><pre>" + post_data + "</pre></body></html>")
        self.server.ticker.setGame(post_data)
        
def run():
    server = HTTPServer(('', 80), TickerHandler)
    server.ticker = Ticker()
    server.ticker.initGame("10")
    server.serve_forever()

if __name__ == "__main__":
    run()