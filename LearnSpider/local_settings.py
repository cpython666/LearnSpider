SECRET_KEY = "your-secret-key"
# settings
# 多语言配置更改语言为中文
LANGUAGE_CODE = "zh-hans"
# 时区
TIME_ZONE = "Asia/Shanghai"
USE_TZ = True
APPEND_SLASH = True

SITE_URL = "http://learnspider.vip"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:63342",  # 允许的前端地址
    "http://localhost:8005",  # 允许的前端地址（如果有必要）
    "http://localhost:5173",  # 允许的前端地址（如果有必要）
    "http://localhost:4173",  # 允许的前端地址（如果有必要）
    "http://localhost:4000",  # 允许的前端地址（如果有必要）
    "http://www.learnspider.vip",
    "http://learnspider.vip",
    "http://localhost",
    "http://127.0.0.1",
]
ALLOWED_HOSTS = [
    "www.learnspider.vip",
    "learnspider.vip",
    "127.0.0.1",
    "localhost",
    "110.42.101.196",
]

# 本地mysql
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "learn_spider",
#         "HOST": "127.0.0.1",
#         "PORT": 3306,
#         "USER": "root",
#         "PASSWORD": "1234",
#     }
# }
