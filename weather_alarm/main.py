import requests
import os
from twilio.rest import Client


API_KEY = os.environ.get('OWM_API_KEY')
account_sid = 'AC924fae9954e1681cb8a9c7883c11d929'
auth_token = os.environ.get('AUTH_TOKEN')

#Buenos Aires coordinates:
LAT = -34.603683
LONG = -58.381557

twilio_number = '+19403505182'
receiver_number = '+541138588855'

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
    'units': 'metric'
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
print(response.url)
data = response.json()
twelve_hours = [data['hourly'][n]['weather'][0]['id'] for n in range(12) if data['hourly'][n]['weather'][0]['id'] < 700]
if len(twelve_hours) > 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, take an umbrella with you 😉.",
        from_=f'{twilio_number}',
        to=f'{receiver_number}'
    )

    print(message.status)


