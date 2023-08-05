import requests
from datetime import datetime
import smtplib

MY_LAT = 19.052839 # Your latitude
MY_LONG = 72.932233 # Your longitude
my_email = "testg2636@gmail.com"
my_password = "wrfmzerlirkdutdq"

def check_in_vision():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False

    #Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = int(str(datetime.now()).split(" ")[1].split(":")[0])

#If the ISS is close to my current position
#and it is currently dark
if sunset < time_now < sunrise:
    if check_in_vision():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="indianamigo717@gmail.com",
                msg=f"Subject:Here's your Weekly Motivaton\n\n LOOK UP!!!,\n You might spot the ISS!"
            )

print(time_now)
#Then send me an email to tell me to look up.
#BONUS: run the code every 60 seconds.

