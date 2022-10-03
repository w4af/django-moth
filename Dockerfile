FROM ubuntu:20.04
MAINTAINER Arthur Taylor <arthur.taylor@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y supervisor joe
RUN apt-get install -y libssl-dev libxml2-dev libxslt1-dev libmemcached-dev
RUN apt-get install -y git-core python3-pip build-essential python3-dev software-properties-common

RUN pip install --upgrade pip
RUN pip install git+https://github.com/coderanger/supervisor-stdout

RUN mkdir -p /var/log/supervisor
RUN useradd ubuntu -d /home/ubuntu

# Django moth configuration
WORKDIR /home/ubuntu/

ADD . /home/ubuntu/django-moth
WORKDIR /home/ubuntu/django-moth
RUN pip install -r requirements.txt

RUN cp /home/ubuntu/django-moth/docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN rm -rf /var/lib/apt/lists/*

EXPOSE 8000
CMD ["/usr/bin/supervisord"]
