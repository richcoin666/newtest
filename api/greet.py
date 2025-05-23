# /api/greet.py
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("🟢 Console running: Python function triggered.")

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
            name = data.get("name", "there")

            print(f"📥 Received name: {name}")

            response = {
                "message": f"Hey {name}, welcome from the Python backend!"
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

            print("✅ Responded successfully.\n")

        except Exception as e:
            print("❌ Error:", str(e))
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = { "error": "Internal Server Error" }
            self.wfile.write(json.dumps(error_response).encode())