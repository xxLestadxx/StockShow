from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import random
import time

bucket = "WattTest"

client = InfluxDBClient(url="http://localhost:8086", token="CKcxAqymiBzP7siL6MqNdmJrAccK7UjUuUrI1umStsgir5jZUnEDmzccjOdb9tILNvqA3GDp_dK_OeTf6QkUcQ==" , org="4d4e5bd125ac30b2")

write_api = client.write_api(write_options=SYNCHRONOUS )
query_api = client.query_api()



# ---------- reading csv data -----------
df = pd.read_csv("data_export_device_single_point_energy.csv", delim_whitespace=True)
print(df)

# ---------- convert the csv data into line protocol and insert into influxDB with time limiter 1, so that you can have a nice graph of static data
# "measurementlevel","levelIdentification/campusId","levelIdentification/buildingId","levelIdentification/floorId","levelIdentification/areaId","levelIdentification/deviceId","measurements/groupBy","measurements/aggregation/func","measurements/aggregation/metric","measurements/time_from","measurements/time_to","measurements/monitoredObject/group","measurements/monitoredObject/values/metric","measurements/monitoredObject/values/value"

# i = 0
# while i < 1000:
#   p = Point("my_measurement").tag("Stock", "Ford").tag("Ticker","F").field("Open", df["Open"][i]).field("High", df["High"][i]).field("Low", df["Low"][i]).field("Close",df["Close"][i])
#   write_api.write(bucket=bucket, record=p)
#   print(i, " opit ", df["Volume"][i])
#   time.sleep(1)
#   i += 1



# i = 1
# while i < 1000:
#   randomNum = random.randrange(20,30) + random.uniform(0,1)
#   p = Point("my_measurement").tag("location", "Prague").field("temperature", randomNum)
#   write_api.write(bucket=bucket, record=p)
#   print(i, " opit ", randomNum)
#   randomNum = random.randrange(20,30) + random.uniform(0,1)
#   p = Point("my_measurement").tag("location", "Varna").field("temperature", randomNum)
#   write_api.write(bucket=bucket, record=p)
#   print(i, " opit ", randomNum)
#   time.sleep(5)
#   i += 1



