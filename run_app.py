"""Serve the ATS Score Engine locally and open it in the default browser.

Usage:
    python run_app.py            # serves on http://localhost:8000 (or the next free port)
    python run_app.py 9000       # serves on a specific port
"""
import http.server
import os
import socketserver
import sys
import webbrowser

DEFAULT_PORT = 8000
MAX_PORT_TRIES = 20


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, fmt, *args):
        # Keep the console quiet except for errors
        if args and str(args[1]).startswith(('4', '5')):
            super().log_message(fmt, *args)


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    # On Windows SO_REUSEADDR lets two servers share a port, which breaks the busy-port fallback
    allow_reuse_address = os.name != 'nt'


def bind(start_port):
    for port in range(start_port, start_port + MAX_PORT_TRIES):
        try:
            return Server(('127.0.0.1', port), Handler), port
        except OSError:
            print(f"Port {port} is busy, trying {port + 1}...")
    sys.exit(f"No free port found between {start_port} and {start_port + MAX_PORT_TRIES - 1}.")


def main():
    # Serve files from the script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    start_port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT

    httpd, port = bind(start_port)
    url = f"http://localhost:{port}"
    print(f"ATS Score Engine running at {url}  (Ctrl+C to stop)")
    webbrowser.open(url)

    with httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == '__main__':
    main()
