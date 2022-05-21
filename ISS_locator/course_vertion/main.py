import requests
from datetime import datetime
import smtplib
import time
MY_LAT = -34.603683 # Your latitude
MY_LONG = -58.381557 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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

time_now = datetime.now().time().hour
print(sunrise, time_now, sunset)

conditions = [
#If the ISS is close to my current position
    (MY_LONG - 5) < iss_longitude < (MY_LONG + 5),
    (MY_LAT - 5) < iss_latitude < (MY_LAT + 5),
# and it is currently dark
    time_now > sunset or time_now < sunrise,
]
is_on = True
while is_on:
    time.sleep(60)
    if all(conditions):
        with smtplib.SMTP('smtp.gmail.com') as connect:
            connect.starttls()
            connect.login(user='mantecadimotta@gmail.com', password='Manteca47+')
            connect.sendmail('mantecadimotta@gmail.com', 'nicolas.salvadores93@gmail.com',
                             msg=f'Subject: ISS Today!\n\n Look at the sky!')
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



