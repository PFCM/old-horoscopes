#! /bin/bash

# deployment script
# builds the image, pushes to docker hub
docker login -e="$DOCKER_EMAIL" -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build -t pfcm/old-horoscopes .
docker push pfcm/old-horoscopes:latest
