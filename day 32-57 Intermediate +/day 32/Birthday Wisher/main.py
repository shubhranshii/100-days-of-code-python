import pandas
from datetime import datetime
import random
import smtplib
import config

MY_EMAIL = config.MY_EMAIL
PASSWORD = config.PASSWORD

today_month=datetime.now().month
today_day=datetime.now().day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    file=f"./letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person= birthdays_dict[today]
    with open (file) as letter_file:
        contents=letter_file.read().replace("[NAME]",birthday_person['name'])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= birthday_person['email'],
                            msg=f"Subject:Happy Birthday\n\n{contents}")

