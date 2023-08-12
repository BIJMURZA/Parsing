import requests
from bs4 import BeautifulSoup


gamename = ['mortal-kombat-11', 'ad-infinitum', 'tekken-7', 'jagged-alliance-3', 'days-gone', 'mortal-kombat-1',
            'no-mans-sky']

for i in range(len(gamename)):
    url = 'https://steampay.com/game/' + gamename[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    soup = soup.find('div', class_="product__current-price")
    if soup.text.split()[0] != "СКОРО":
        print(gamename[i] + ' ' + soup.text.split()[0] + "₽")
    else:
        print(gamename[i] + ' ' + "Нет в наличии")