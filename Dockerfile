FROM docker.io/python:3.7-alpine

WORKDIR /app
VOLUME /app

CMD ["python3", "-u", "/app/main.py"]
