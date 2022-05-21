# import smtplib
#
# email_1 = "mantecadimotta@gmail.com"
# password_1 = 'Manteca47+'
# email_2 = "mantecasalvadores@yahoo.com"
# password_2 = 'bdbjonelusaxqjsj'
#
# with smtplib.SMTP('smtp.gmail.com') as connect_1:
# #with smtplib.SMTP('smtp.mail.yahoo.com') as connect_2:
#     connect_1.starttls()
#     connect_1.login(user=email_1, password=password_1)
#     connect_1.sendmail(from_addr=email_1,
#                        to_addrs=email_2,
#                        msg="Subject:wasaaaaaa\n\ntodo bien?")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
# day = now.day
# print(day)
# my_bd = dt.datetime(year=1993, month=8, day=13)
# print(my_bd)

import datetime as dt
import smtplib
import random

#-----------Selecting the quote of the day---------
with open('quotes.txt') as quotes:
    all_quotes = quotes.read()
    list_of_quotes = all_quotes.split("\n")
    quote_of_the_day = random.choice(list_of_quotes)
    print(quote_of_the_day)
#-----------Checking the day of the weeek---------
now = dt.datetime.now()
day_of_the_week = now.day

#----------Sending the email----------------------
email_1 = "mantecadimotta@gmail.com"
password_1 = 'Manteca47+'
email_2 = "mantecasalvadores@yahoo.com"
password_2 = 'bdbjonelusaxqjsj'

if day_of_the_week == 6:
    with smtplib.SMTP('smtp.gmail.com') as connect_1:
        connect_1.starttls()
        connect_1.login(user=email_1, password=password_1)
        connect_1.sendmail(from_addr=email_1,
                           to_addrs=email_2,
                           msg=f"Subject:Quote of the day\n\n{quote_of_the_day}")
