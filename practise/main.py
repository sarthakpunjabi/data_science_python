# with open("weather_data.csv") as data:
#     Data = data.readlines()
#     print(Data)

# import csv
# with open("weather_data.csv") as Data:
#     data = csv.reader(Data)
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))  

#     print(temperatures)

# from numpy import average
# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# data_list = data['temp'].to_list()
# data_temp = data.temp
# print(data_temp.max()*(9/5)+30)

import pandas as pd

data = pd.read_csv("squirrel.csv")
group = data['Primary Fur Color'].value_counts()
print(group.to_csv("main.csv"))