import http.server
import socketserver
import os
import sys

def run_server(port, directory):
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/":
                self.send_response(301)
                self.send_header('Location', '/auth')
                self.end_headers()
            else:
                return http.server.SimpleHTTPRequestHandler.do_GET(self)

    os.chdir(directory)

    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python server.py <PORT> <DIRECTORY>")
    else:
        PORT = int(sys.argv[1])
        DIRECTORY = sys.argv[2]
        run_server(PORT, DIRECTORY)

