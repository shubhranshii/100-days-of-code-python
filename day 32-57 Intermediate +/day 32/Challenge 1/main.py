import smtplib
import datetime as dt
import random
import config

MY_EMAIL = config.MY_EMAIL
PASSWORD = config.PASSWORD

now = dt.datetime.now()
today = now.weekday()
if today == 0:

    with open("quotes.txt") as file:
        quotes_list = file.readlines()

    todays_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="shlopoke@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n{todays_quote}")
