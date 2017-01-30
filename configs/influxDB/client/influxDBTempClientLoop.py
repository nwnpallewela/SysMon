#!/usr/bin/python
import time
#import serial
import datetime
from influxdb import InfluxDBClient

#Setup some constants with InfluxDB Host and Database name
INFLUXDB_HOST = '172.17.0.2'
INFLUXDB_NAME = 'temperature_db'

#Connect to Serial Port for communication
#ser = serial.Serial('COM15', 9600, timeout=0)

#Setup a loop to send Temperature values at fixed intervals
#in seconds
fixed_interval = 10
while 1:
	#temperature value obtained from Arduino + LM35 Temp Sensor
	temperature_c = 28.2 #ser.readline()
	#Timestamp
	timestamp = datetime.datetime.utcnow().isoformat()

	#Station Name that is recording the temperature
	station_name = "S2"

	#Initialize the InfluxDB Client
	client = InfluxDBClient(INFLUXDB_HOST,'8086','','',INFLUXDB_NAME)

	#Write a record
	json_data = [
	{
	"measurement":"temperature",
	"time":timestamp,
	"tags": {
	"Station":station_name
	},

	"fields": {
	"value":temperature_c
	}
	}
	]

	bResult = client.write_points(json_data)
	print("Result of Write Data : ",bResult)
	time.sleep(fixed_interval)
	
print "Good bye!"
