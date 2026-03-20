FROM python:3.8-slim
RUN pip install --no-cache-dir flask==2.2.2
COPY app.py /app.py
# Запускаем напрямую через python без лишних оболочек
ENTRYPOINT ["python3", "/app.py"]
