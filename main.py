from email import header
from urllib import response
import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/HP-6-Cores-Graphics-Portable-Windows/dp/B09CD34PB5/ref=sr_1_2_sspa?crid=2JELVI72HUUR4&keywords=hp+15s+ryzen+5&qid=1644810290&sprefix=hp+15s+ryzen+%2Caps%2C583&sr=8-2-spons&psc=1&smid=A1LZN806TROZ37&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQ0NKT1VQNzhLMVoyJmVuY3J5cHRlZElkPUEwODU3MTQzMzVEMVBENkVPR0VGQyZlbmNyeXB0ZWRBZElkPUEwODY2OTAwMjBXNU9VRUU4TldRWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

user_price_entry = input('Enter price you like : ')

header = {
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
}

my_email = "YOUR_EMAIL_ADD"
my_password = "YOUR_PASSWORD"

response = requests.get(url=URL,headers=header)

soup = BeautifulSoup(response.content,"lxml")
print(soup.prettify())

price_of_product = soup.find(name="span",class_="a-offscreen").get_text()
price_split = price_of_product.split("$")[1]
remove_coma = price_split.replace(",","")
price_conversion = float(remove_coma)
print(price_conversion)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_conversion<=user_price_entry:
    conection = smtplib.SMTP("smtp.gmail.com")
    conection.starttls()
    conection.login(my_email,my_password)
    conection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"your product price alert \n\n Produt:{title}\n Link{URL} "
    )

