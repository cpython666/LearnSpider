# 选择基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /usr/src/app

# 复制项目文件
COPY . .

# 安装依赖
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 执行数据库迁移
RUN python manage.py migrate

# 指定运行命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]