import pandas as p
from random import choice
import datetime as dt
import smtplib

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.text"]
##################### Extra Hard Starting Project ######################
my_email = "testg2636@gmail.com"
my_password = "wrfmzerlirkdutdq"

data = p.read_csv("birthdays.csv")
date = data.to_dict(orient='records')
print(date)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
# print(month, day, year)

if month == date[0]["month"] and day == date[0]["day"]:
    with open(f"{choice(letters)}") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", "Aditya")
        # print(letter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="testg2636@yahoo.com",
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




