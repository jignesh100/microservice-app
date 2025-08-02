FROM python:3.9-slim

WORKDIR /product_service

COPY requirements.txt .

RUN pip install --no-cache-dir requirements.txt

COPY . .

RUN ["python","app.py"]

EXPOSE 5002

