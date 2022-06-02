FROM python:latest

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install libboost-all-dev -y
RUN apt-get update
RUN apt-get install cmake -y
RUN pip install dlib

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# COPY . .
