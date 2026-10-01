# import http.server
# import socketserver
# import webbrowser
# import os

# PORT = 8000

# class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def end_headers(self):
#         self.send_header('Access-Control-Allow-Origin', '*')
#         super().end_headers()

# # Set working directory to the script's folder
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(f"Server starting at http://localhost:{PORT}")
# webbrowser.open(f"http://localhost:{PORT}")

# with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
#     try:
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print("\nServer stopped.")