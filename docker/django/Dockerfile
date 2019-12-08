FROM python:3.8.0
ENV PYTHONUNBUFFERED 1

RUN mkdir /code && apt-get update && apt-get install curl rsyslog

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./sample_project /code/
