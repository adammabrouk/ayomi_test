# base image
FROM python:3.6.5

MAINTAINER Adam

ADD . /usr/src/ayomi_test/

WORKDIR /usr/src/ayomi_test

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD exec ./manage.py runserver 0.0.0.0:8000


