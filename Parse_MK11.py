import requests
from bs4 import BeautifulSoup

url = 'https://gameray.ru/mortal-kombat-11/?utm_source=hot-game.info&utm_medium=affiliate&partner=156'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
f = soup.find('span', itemprop="price")
print(f.text + "₽")