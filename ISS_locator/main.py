import requests
import datetime as dt


MY_LAT = -34.603683
MY_LONG =
# request = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(request) # 200 means request successeful
# request.raise_for_status() #Explain the error in case request not successful
# data = request.json()
# print(data)
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
print(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}")
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

my_dt = dt.datetime
now = my_dt.now().time().hour
print(sunrise)
print(now)
print(sunset)
