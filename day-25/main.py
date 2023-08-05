# # with open("weather_data.csv", "r+") as weather_data:
# #     name = ""
# #     # content = weather_data.read()
# #     # content = content.replace("\n", name.strip())
# #     data = weather_data.readlines()
# #
# # # with open("./weather_data_1.csv", "w") as weather_data_1:
# # #     weather_data_1.write(content)
# # # data_in_content = content.readlines()
# #
# # # print(content)
# # print(data)
#
# # for data in content:
# # weather_data.write(content)
# #
# # import csv
# #
# # with open("weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temprature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temprature.append(int(row[1]))
# #     print(temprature)
#
import pandas
# # data = pandas.read_csv("weather_data.csv")
# # # temp_list = data["temp"].to_list()
# # # avg_temp = sum(temp_list) / len(temp_list)
# # # print(int(avg_temp))
# #
# # # print(data["temp"].max())
# # # print(data[data.temp == data.temp.max()])
# #
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# # monday_temp = monday_temp *9/5+32
# # print(monday_temp)
# # print(monday.temp*9/5+32)
#
# IDENTITY = {
#     "SID000001": {
#         "name": "Aditya Ravindra Dikonda",
#         "branch": "Electronics & Telecommunications Engineering",
#         "year": "2022-2026",
#         "birth_date": "10-February-2005",
#         "gender": "male",
#         "phone_number": "9167965566",
#         "address": "709/1B, Koyna CHS, Mankhurd, Mumbai 400043.",
#         "e-mail": "adityadikonda10@gmail.com",
#         "GST-Email": "adityardextc122@gst.sies.edu.in",
#
#     },
#     "SID000002": {
#         "name": "Riya Praveenkumar Alle",
#         "branch": "Electronics & Telecommunications Engineering",
#         "year": "2022-2026",
#         "birth_date": "10-August-2004",
#         "gender": "female",
#         "phone_number": "",
#         "address": "709/1B, Koyna CHS, Mankhurd, Mumbai 400043.",
#         "e-mail": "@gmail.com",
#         "GST-Email": "extc122@gst.sies.edu.in",
#
#     },
#     "SID000003": {
#         "name": "",
#         "branch": "Electronics & Telecommunications Engineering",
#         "year": "2022-2026",
#         "birth_date": "",
#         "gender": "male",
#         "phone_number": "",
#         "address": "",
#         "e-mail": "@gmail.com",
#         "GST-Email": "extc122@gst.sies.edu.in",
#
#     },
#     "SID000004": {
#         "name": "",
#         "branch": "Electronics & Telecommunications Engineering",
#         "year": "2022-2026",
#         "birth_date": "",
#         "gender": "male",
#         "phone_number": "",
#         "address": "",
#         "e-mail": "@gmail.com",
#         "GST-Email": "extc122@gst.sies.edu.in",
#
#     },
#     "SID000005": {
#         "name": "",
#         "branch": "Electronics & Telecommunications Engineering",
#         "year": "2022-2026",
#         "birth_date": "",
#         "gender": "male",
#         "phone_number": "",
#         "address": "",
#         "e-mail": "@gmail.com",
#         "GST-Email": "extc122@gst.sies.edu.in",
#
#     },
# }
# data = pandas.DataFrame(IDENTITY)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(gray)
print(cinnamon)
print(black)

data_dict = {
    "Fur Color": ["Cinnamon", "Black", "Gray"],
    "Count": [cinnamon, black, gray]
}

squirrel_color_data = pandas.DataFrame(data_dict)
squirrel_color_data.to_csv("Sqirrel_color.csv")
print(data_dict)