#! /bin/bash
set -e
# deployment script
# builds the image, pushes to docker hub
docker login -e="$DOCKER_EMAIL" -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build -t pfcm/old-horoscopes:$COMMIT .
docker tag -f pfcm/old-horoscopes:$COMMIT pfcm/old-horoscopes:latest
docker tag pfcm/old-horoscopes:$COMMIT pfcm/old-horoscopes:build-$TRAVIS_BUILD_NUMBER
docker push pfcm/old-horoscopes
