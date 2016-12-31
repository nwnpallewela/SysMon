#!/bin/bash
echo "==================================="
echo "Stoping InfluxDB docker container"
echo "==================================="

docker stop influxdb
docker rm influxdb

echo "================================" && \
echo "Stoping Grafana docker container" && \
echo "================================"

docker stop grafana
docker rm grafana
