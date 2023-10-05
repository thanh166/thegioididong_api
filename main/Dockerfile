FROM python:3.9.16-slim-buster
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
WORKDIR /app
COPY . /app
RUN pip install flask requests
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]




