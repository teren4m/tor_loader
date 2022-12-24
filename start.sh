#!/bin/bash

app_name="tor_proxy"

docker build -t ${app_name} .

docker rm $(docker ps -a -q)
docker run -d -p 4500:4500 --name=${app_name} ${app_name} 
