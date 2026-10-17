"""لوحة تحكم بوت المراجحة - web_app.py
خادم ويب بسيط يعرض لوحة التحكم
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = int(os.environ.get("PORT", 8000))

print(f"Starting dashboard on port {PORT}...")

HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler).serve_forever()
