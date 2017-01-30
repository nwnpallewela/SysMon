import datetime

from influxdb import InfluxDBClient

#Setup some constants with InfluxDB Host and Database name
INFLUXDB_HOST = '172.17.0.2'
INFLUXDB_NAME = 'temperature_db'

#Sample values -- these will be read from sensor
temperature_c = 27.8

#Timestamp
timestamp = datetime.datetime.utcnow().isoformat()

#Station Name that is recording the temperature
station_name = "S2"

#Initialize the InfluxDB Client
client = InfluxDBClient(INFLUXDB_HOST,'8086','','',INFLUXDB_NAME)

#Query Existing Values
result = client.query('SELECT * FROM temperature')
points = list(result.get_points(measurement='temperature'))
for point in points:
   print('Station = ',point['Station'],'Value = ',point['value'])

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
