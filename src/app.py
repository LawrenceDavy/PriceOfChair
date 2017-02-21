__author__ = 'aiwass'

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-murray-ergonomic-office-chair-black/p1919328")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 400:
    print("Buy the chair!!!")
    print("The current price is {}".format(string_price))
else:
        print("You cannot afford to buy this chair")


# <span itemprop="price" class="now-price"> £229.00 </span>

