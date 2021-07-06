import yfinance as yf 
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import time



# Setup database
bucket = "WattTest"

client = InfluxDBClient(url="http://localhost:8086", token="CKcxAqymiBzP7siL6MqNdmJrAccK7UjUuUrI1umStsgir5jZUnEDmzccjOdb9tILNvqA3GDp_dK_OeTf6QkUcQ==" , org="4d4e5bd125ac30b2")

write_api = client.write_api(write_options=SYNCHRONOUS )
query_api = client.query_api()

# Setup Stock
F =  yf.Ticker("F")


# # get historical market data
# hist = F.history(period="max")

# # show dividends 
# print( hist )



# --------- writing into csv ---------


# df = pd.DataFrame(hist)
# print (df.to_csv)
# dfStr = df.to_csv
# f = open("demofile2.txt", "a")
# f.write(df.to_csv(index=False))
# f.close()



# ---------- reading csv data -----------
df = pd.read_csv("demofile2.txt", delim_whitespace=True)

# ---------- convert the csv data into line protocol and insert into influxDB with time limiter 1, so that you can have a nice graph of static data
i = 0
while i < 1000:
  p = Point("my_measurement").tag("Stock", "Ford").tag("Ticker","F").field("Open", df["Open"][i]).field("High", df["High"][i]).field("Low", df["Low"][i]).field("Close",df["Close"][i])
  write_api.write(bucket=bucket, record=p)
  print(i, " opit ", df["Volume"][i])
  time.sleep(1)
  i += 1




