# 使用官方 Python 基础镜像
FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY . /app

# 创建 Streamlit 配置文件路径
RUN mkdir -p ~/.streamlit

# 添加配置文件
COPY config.toml ~/.streamlit/config.toml

# 安装 Streamlit
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple streamlit  aiohttp requests
# 暴露 Streamlit 默认端口
EXPOSE 31001

# 设置 Streamlit 配置（可选，防止运行时报错）
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=31001 \
    STREAMLIT_SERVER_ENABLECORS=false

# 启动 Streamlit 应用
CMD ["python", "-m", "streamlit", "run", "/app/ui.py"]
