#!/bin/bash

docker-compose down
docker rm -f $(docker ps --filter name=doccano -a -q)
docker volume rm doccano_static_volume
docker volume rm doccano_www
docker-compose -f docker-compose.prod.yml build
nohup docker-compose -f docker-compose.prod.yml up --remove-orphans > doccano_log.out &