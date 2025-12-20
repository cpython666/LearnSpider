import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import hashlib
import hmac
import base64

SALT = b"WmSalt123"
SECRET = "WmSecretKey-2025"
PEPPER = "Glass-Edge"
EXPECTED = "JKPb5sxlg3sWO6RPLwtwzupvQo2M2PC2LG8CVrYjI2I="

def calc(pwd: str) -> str:
    key = hashlib.pbkdf2_hmac("sha256", pwd.encode(), SALT, 200000, 32)
    mac = hmac.new(key, (SECRET + PEPPER).encode(), hashlib.sha256).digest()
    return base64.b64encode(mac).decode()

class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type, x-client-auth")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, GET")

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else:
            self.send_response(404)
            self._cors()
            self.end_headers()

    def do_POST(self):
        if self.path != "/api/login":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        token = self.headers.get("X-Client-Auth") or ""
        ok = token == EXPECTED
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": ok}).encode())

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8091), H).serve_forever()
