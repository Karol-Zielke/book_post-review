FROM alpine:3.12
MAINTAINER Karol Zielke

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt/ requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app/ app

RUN adduser -D user
USER user
