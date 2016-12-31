#!/bin/bash
echo "---------------------------------------"
echo "Starting docker container with influxDB"
echo "---------------------------------------"
sudo docker run -d -p 8083:8083 -p 8086:8086   -e PRE_CREATE_DB="wadus"   --expose 8090 --expose 8099   --name influxdb   tutum/influxdb

echo "---------------------------------------"
echo "Starting docker container with Grafana"
echo "---------------------------------------"
sudo docker run -d -p 3000:3000   --link influxdb:influxdb   --name grafana   grafana/grafana


