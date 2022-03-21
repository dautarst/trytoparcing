from urllib import response
from bs4 import BeautifulSoup   
import requests
from requests import get
import time
import random

url = 'https://auto.ru/cars/kia/soul/all/?transmission=AUTOMATIC'
auto = []
namepage = page
count = 1
while count <= 100:
    url = 'https://auto.ru/cars/kia/soul/all/?transmission=AUTOMATIC' + str(namepage) + str('=') + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    auto_data = html_soup.find_all('div', class_="ListingItem__main")
    if auto_data != []:
        auto.extend(auto_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count += 1

print(len(auto))