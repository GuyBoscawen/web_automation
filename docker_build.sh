#!/bin/bash
set -e

mkdir buildContext

cp ./deployment/Dockerfile ./buildContext/Dockerfile
cp ./deployment/requirements.txt ./buildContext
cp -r ./app ./buildContext

ls -al buildContext
cd buildContext
echo "balh"
docker build .
echo "balh"
docker push guyboscawen/public:nate

rm -rf buildContext
