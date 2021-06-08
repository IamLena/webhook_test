import argparse
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

USEDPORT = 4567

class S(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		message = json.loads(self.rfile.read(content_length)) ## it is a dictionary
		self._set_headers()
		action = message["action"]	#closed
		from_branch = message["pull_request"]["head"]["ref"]	# in staging (feature branch SD-873)
		to_branch = message["pull_request"]["base"]["ref"]		# main (in staging)
		print(action + ": " + from_branch + " -> " + to_branch)

def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=USEDPORT):
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
		default=USEDPORT,
		help="Specify the port on which the server listens",
	)
	args = parser.parse_args()
	run(addr=args.listen, port=args.port)
