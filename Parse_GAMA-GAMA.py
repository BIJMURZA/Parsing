import requests
from bs4 import BeautifulSoup

url = "https://gama-gama.ru/detail/jagged-alliance-3/"
resourse = requests.get(url)
soup = BeautifulSoup(resourse.text, 'lxml')
soup = soup.find('a', class_="btn-large btn-buy js_buy")

print(soup.text.split()[2] + "₽")