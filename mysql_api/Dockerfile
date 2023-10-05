FROM python:3.9.16-slim-buster
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn mysql-connector-python python-multipart requests
CMD uvicorn main:app --host 0.0.0.0 --port 9001