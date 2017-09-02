FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y python3-dev libpq-dev build-essential
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt --upgrade
ADD . /code/