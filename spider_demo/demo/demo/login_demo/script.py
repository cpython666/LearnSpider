import sys, hashlib, hmac, base64
SALT = b'WmSalt123'
SECRET = 'WmSecretKey-2025'
PEPPER = 'Glass-Edge'

def calc(pwd: str) -> str:
    key = hashlib.pbkdf2_hmac('sha256', pwd.encode(), SALT, 200000, 32)
    mac = hmac.new(key, (SECRET + PEPPER).encode(), hashlib.sha256).digest()
    return base64.b64encode(mac).decode()

if __name__ == '__main__':
    pwd = "1234"
    print(calc(pwd))
