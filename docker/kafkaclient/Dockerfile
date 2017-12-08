FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install virtualenv python3-virtualenv python3-pip
RUN virtualenv --python=/usr/bin/python3 /tmp/virtualenv

RUN /tmp/virtualenv/bin/pip install kafka==1.3.5

COPY ./docker/kafkaclient/kafkaclient.py /tmp/

ENTRYPOINT sleep 5 && /tmp/virtualenv/bin/python /tmp/kafkaclient.py
