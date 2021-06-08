import argparse
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.

        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        # post_data = self.rfile.read(content_length) # <--- Gets the data itself
        # self._set_headers()
        # self.wfile.write("<html><body><h1>POST!</h1><pre>" + post_data + "</pre></body></html>")

        message = json.loads(self.rfile.read(content_length)) ## it is a dictionary

        # add a property to the object, just to mess with data
        # message['received'] = 'ok'

        # send the message back
        self._set_headers()
        msg = json.dumps(message)
        action = message["action"]	#closed
        from_branch = message["pull_request"]["head"]["ref"]	# in staging (feature branch SD-873)
        to_branch = message["pull_request"]["base"]["ref"]		# main (in staging)
        print(from_branch + " -> " + to_branch)
        # print(msg)
        # self.wfile.write("<html><body><h1>POST!</h1><pre>ololo</pre></body></html>")


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=4567,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
