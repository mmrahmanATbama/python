
import pandas
from collections import Counter

data = pandas.read_csv("Squirrel_Data.csv")
squirrel_colors = data["Primary Fur Color"].to_list()
colors = dict(Counter(squirrel_colors))
# squirrel_data = pandas.DataFrame([colors])
# squirrel_data = pandas.DataFrame(colors)
fur_color = list(colors.keys())
count = list(colors.values())

squirrels = {
    "Fur Color": fur_color,
    "Count": count
}

datas = (pandas.DataFrame(squirrels))
datas.to_csv("new_data.csv")


# with open("Weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
#
# with open("Weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1].isdigit() :
#             temperature.append(int(row[1]))
#
# print(temperature)

# unique_color = set(squirrel_colors)
# colors = list(unique_color)


# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
#
# average_temp = sum(temp_list) / len(temp_list)
#
# print(average_temp)
# print(temp_list)
# maximum = data["temp"].max()
# print(maximum)
# print(data.condition)
#
# # get data from rows:
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
#
# print(data[data.temp == data.temp.max()])
# print(monday.condition)

# create a dataframe from scratch
# data_dict = {
#     "students": ["a", "b", "c"],
#     "score": [1, 2, 3]
# }
#
# data = (pandas.DataFrame(data_dict))
# data.to_csv("new_data.csv")
