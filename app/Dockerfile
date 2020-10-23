FROM ubuntu:20.04

CMD ["python3"]

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN apt-get update && apt-get install python3 python3-dev python3-pip python3-psycopg2 unixodbc-dev musl-dev gcc libc-dev g++ libffi-dev -y -qq\
  && pip3 install --upgrade --no-cache-dir pip setuptools \
  && pip3 install --no-cache-dir -r requirements.txt \
  && ln -s /usr/bin/python3 /usr/bin/python 
