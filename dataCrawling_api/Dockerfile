FROM python:3.9.16-slim-buster
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn requests bs4 mysql-connector-python
CMD uvicorn main:app --host 0.0.0.0 --port 8001