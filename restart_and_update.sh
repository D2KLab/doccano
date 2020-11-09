#!/bin/bash

docker-compose down --remove-orphans
docker container rm -f $(docker ps --filter name=doccano -a -q)
docker image rm -f $(docker image ls --format="{{.Repository}} {{.ID}}" | grep "^doccano" | cut -d' ' -f2)
# uncomment if you want to delete also networks
#docker network rm $(docker network ls --format="{{.Name}} {{.ID}}" | grep "^doccano" | cut -d' ' -f2)
docker volume rm doccano_static_volume
docker volume rm doccano_www
docker-compose -f docker-compose.prod.yml build
nohup docker-compose -f docker-compose.prod.yml up --remove-orphans > doccano_log.out &
