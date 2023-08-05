import requests
from datetime import datetime
MY_LAT = 19.052854
MY_LNG = 72.932218

paramaters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,

}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=paramaters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now = datetime.now()

print(time_now)
print(sunrise)
print(sunset)




