from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

bucket = "WattTest"

client = InfluxDBClient(url="http://localhost:8086", token="CKcxAqymiBzP7siL6MqNdmJrAccK7UjUuUrI1umStsgir5jZUnEDmzccjOdb9tILNvqA3GDp_dK_OeTf6QkUcQ==" , org="4d4e5bd125ac30b2")

write_api = client.write_api(write_options=SYNCHRONOUS )
query_api = client.query_api()


while True:
  #Temperature
  randomNum = random.randrange(20,30) + random.uniform(0,1)
  p = Point("Building").tag("location", "Prague").field("temperature", randomNum)
  write_api.write(bucket=bucket, record=p)
  print(" opit temp ", randomNum)
  randomNum = random.randrange(20,30) + random.uniform(0,1)
  p = Point("Building").tag("location", "Varna").field("temperature", randomNum-5)
  write_api.write(bucket=bucket, record=p)
  print(" opit temp ", randomNum)
  
  #PPM
  randomNum = random.randrange(900,1100) + random.uniform(0,1)
  p = Point("Building").tag("location", "Prague").field("parts_per_notation", randomNum)
  write_api.write(bucket=bucket, record=p)
  print(" opit ppm ", randomNum)
  randomNum = random.randrange(800,1000) + random.uniform(0,1)
  p = Point("Building").tag("location", "Varna").field("parts_per_notation", randomNum)
  write_api.write(bucket=bucket, record=p)
  print(" opit  ppm ", randomNum)
  

  #electricity consumption
  randomNum = random.randrange(3,8) + random.uniform(0,1)
  p = Point("Building").tag("location", "Prague").field("electricity_consumption", randomNum)
  write_api.write(bucket=bucket, record=p)
  print(" opit el cons ", randomNum)
  

  #electricity efficiency 
  randomNum = random.randrange(3,8) + random.uniform(0,1)
  p = Point("Building").tag("location", "Prague").field("electricity_consumption_efficiency", randomNum)
  write_api.write(bucket=bucket, record=p)
  print( " opit el eff ", randomNum)
  randomNum = random.randrange(1,5) + random.uniform(0,1)
  p = Point("Building").tag("location", "Varna").field("electricity_consumption_efficiency", randomNum)
  write_api.write(bucket=bucket, record=p)
  print(" opit el eff ", randomNum)
  time.sleep(60)
