# Basic importing of data Python script
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horse power",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers
print("First 10 records \n")
print(df.head(10))
print("Last 10 records \n")
print(df.tail(10))
#df.to_csv("/Users/ferrycosv/PycharmProjects/Python_course/imports-85.csv")

# Data basic statistics quick look
basic_statistics = df.describe(include="all")

# Top 30 and bottom 30 rows
print(df.info())

