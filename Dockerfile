FROM python:latest

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
#
RUN mkdir app
WORKDIR app
#

ADD redis_test.py /app
CMD python redis_test.py