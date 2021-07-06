from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

bucket = "WattTest"

client = InfluxDBClient(url="http://localhost:8086", token="CKcxAqymiBzP7siL6MqNdmJrAccK7UjUuUrI1umStsgir5jZUnEDmzccjOdb9tILNvqA3GDp_dK_OeTf6QkUcQ==" , org="4d4e5bd125ac30b2")

write_api = client.write_api(write_options=SYNCHRONOUS )
query_api = client.query_api()

i = 1
while i < 1000:
  randomNum = random.randrange(20,30) + random.uniform(0,1)
  p = Point("my_measurement").tag("location", "Prague").field("temperature", randomNum)
  write_api.write(bucket=bucket, record=p)
  print(i, " opit ", randomNum)
  randomNum = random.randrange(20,30) + random.uniform(0,1)
  p = Point("my_measurement").tag("location", "Varna").field("temperature", randomNum)
  write_api.write(bucket=bucket, record=p)
  print(i, " opit ", randomNum)
  time.sleep(5)
  i += 1



