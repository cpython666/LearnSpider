# 选择基础镜像
#FROM python:3.11
FROM python:3.11-slim
# 设置工作目录
WORKDIR /app

# 更新pip到最新版本
RUN pip install --upgrade pip

# 复制项目文件
COPY . .
# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# 指定运行命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]