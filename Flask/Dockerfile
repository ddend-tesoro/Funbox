FROM python:3.7-alpine
MAINTAINER Grigory G.

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir app
WORKDIR app
#
ADD funbox.py /app
#ADD redis_test.py /app
#CMD python redis_test.py
#
CMD python funbox.py