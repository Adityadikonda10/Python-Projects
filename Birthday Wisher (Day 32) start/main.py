import datetime as dt
import smtplib
from random import choice


my_email = "testg2636@gmail.com"
my_password = "wrfmzerlirkdutdq"
with open("quotes.txt") as f:
    quote = choice(f.readlines())
print(quote)

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="testg2636@yahoo.com",
            msg=f"Subject:Here's your Weekly Motivaton\n\n{quote}"
        )