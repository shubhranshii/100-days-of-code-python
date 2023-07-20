#import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1]=="temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data= pandas.read_csv("weather_data.csv")
# print(data["temp"])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colours=["Gray","Cinnamon", "Black"]
# print(data)
# count=[0,0,0]
# for ind in data.index:
#     if data["Primary Fur Color"][ind]=="Gray":
#         count[0]+=1
#     elif data["Primary Fur Color"][ind] == "Cinnamon":
#         count[1] += 1
#     elif data["Primary Fur Color"][ind] == "Black":
#         count[2] += 1

gray_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels=len(data[data["Primary Fur Color"]=="Black"])

new_data = {'color': colours, 'count': [gray_squirrels, cinnamon_squirrels, black_squirrels]}
df=pandas.DataFrame(new_data)
print(df)
df.to_csv("squirrel_count.csv")
# print(colours)
# print(count)