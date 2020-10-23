FROM node:13.7

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install git python3 make g++ -y -qq \
  # && npm install -g yarn@latest \
  && yarn install \
  && yarn build \
  && apt-get purge git make g++ -y -qq
