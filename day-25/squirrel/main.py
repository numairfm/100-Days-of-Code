import pandas as pd

# CSV = "weather_data.csv"
# with open(CSV, "r") as csv:
#     data = csv.readlines()
#     print(data)

# import csv

# with open(CSV, "r") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for temperature in data:
#         try:
#             temperatures.append(int(temperature[1]))
#         except ValueError:
#             pass
#     print(temperatures)
#     for row in data:
#         print(row)

CSV = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

df = pd.read_csv(CSV)
cnt = df["Primary Fur Color"].value_counts()

gray_cnt = int(cnt[cnt.keys()[0]])
red_cnt = int(cnt[cnt.keys()[1]])
black_cnt = int(cnt[cnt.keys()[2]])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_cnt, red_cnt, black_cnt],
}
print(data_dict)

ndf = pd.DataFrame(data_dict)
ndf.to_csv("squirrel_count.csv")
