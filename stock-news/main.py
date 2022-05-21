import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#---------Stocks----------
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = '2GNKAINK5RLD5T2I'
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': STOCK_API_KEY,
    #'interval': '60min'
}
#-----------News----------------
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = '3f2f78666ce64e3e8cde5b3b6fd229bd'
news_parameters = {
    'apiKey': NEWS_API_KEY,
    'q': COMPANY_NAME,
    'searchIn': 'title,description',
    'lenguaje': 'en',
    'pageSize': 3,
}
r = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
r.raise_for_status()
stock_data = r.json()
#print(r.url)
yesterday = list(stock_data['Time Series (Daily)'])[0]
previous = list(stock_data['Time Series (Daily)'])[1]
yesterday_price = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
previous_price = float(stock_data['Time Series (Daily)'][previous]['4. close'])

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
dif_in_porcent = round(((yesterday_price - previous_price) * 100) / previous_price, 1)
if dif_in_porcent > 0:
    up_or_down = '🔺'
else:
    up_or_down = '🔻'
print(yesterday_price, previous_price, dif_in_porcent)
if abs(dif_in_porcent) > 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    r = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    r.raise_for_status()
    news_data = r.json()
    #print(r.url)
    news_headlines = [news_data['articles'][n]['title'] for n in range(3)]
    news_description = [news_data['articles'][n]['description'] for n in range(3)]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    TWILIO_NUM = '+19403505182'
    MY_NUM = '+541138588855'
    for num in range(len(news_headlines)):
        message = client.messages.create(
            body=f"{STOCK}: {up_or_down}{dif_in_porcent}% \n{news_headlines[num]}\n{news_description[num]}.",
            from_=TWILIO_NUM,
            to=MY_NUM,
        )

        print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

