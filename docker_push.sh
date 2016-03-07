#! /bin/bash

# deployment script
# builds the image, pushes to docker hub
docker login -e="$DOCKER_EMAIL" -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build -t pfcm/old-horoscopes:$COMMIT .
docker tag pfcm/old-horoscopes:$COMMIT pfcm/old-horoscopes:latest
docker push pfcm/old-horoscopes
