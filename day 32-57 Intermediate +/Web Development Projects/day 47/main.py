import requests
from bs4 import BeautifulSoup
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("jgiiauwtdkuttabb")

PRODUCT_URL= "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
"Accept-Language":"en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7"

}
response= requests.get(url=PRODUCT_URL, headers=headers)
soup=BeautifulSoup(response.text,"html.parser")

price_whole=soup.find(class_="a-price-whole").text
price_decimal=soup.find(class_="a-price-fraction").text
price=float(f"{price_whole}{price_decimal}")

product_title=soup.find(id="productTitle").text.strip()

if price < 100.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now ${price}\n{PRODUCT_URL}".encode('utf-8'))