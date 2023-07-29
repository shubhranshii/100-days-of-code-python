import requests
from twilio.rest import Client
import config

ACCOUNT_SID = config.account_sid
AUTH_TOKEN = config.auth_token
MY_PHONE = config.my_phone

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = config.stock_api_key
NEWS_API_KEY = config.news_api_key

stock_params = {'function': 'TIME_SERIES_DAILY',
                'symbol': STOCK_NAME,
                "apikey": STOCK_API_KEY}

r = requests.get(url=STOCK_ENDPOINT, params=stock_params)
r.raise_for_status()
data = r.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])

diff = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "None"
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

per_diff = diff / day_before_yesterday_closing_price * 100
print(per_diff)

if abs(per_diff) > 4:

    news_params = {'apiKey': NEWS_API_KEY,
                   'qInTitle': COMPANY_NAME,
                   'language': 'en',
                   'page': 1}

    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()['articles']

    if len(news_data) > 3:
        required_articles = news_data[:3]
    else:
        required_articles = news_data

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    formatted_articles = [
        f"{STOCK_NAME}:{up_down}{per_diff}%\nHeadline:{article['title']} \nBrief:{article['description']}" for article
        in
        required_articles]
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12295973709',
            to=MY_PHONE
        )

    # Optional TODO: Format the message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
