# place the csv file content into a list named data
#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# Create a list using csv library

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = [int(temp[1]) for temp in data if temp[1] != "temp"]
#
#     print(temperature)

# Using pandas library, the most effective and shortest way of working with csv files

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()

# data discovery phase of EDA
avg_temp = round(data["temp"].mean(), 2)
print("The average temperature is: ", avg_temp)

max_temp = data["temp"].max()
print("The max temperature is: ", max_temp)
