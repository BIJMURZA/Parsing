import requests
from bs4 import BeautifulSoup

gamename = ['mortal-kombat-11', 'ad-infinitum', 'tekken-7', 'jagged-alliance-3', 'days-gone', 'mortal-kombat-1',
            'no-mans-sky', 'The Witcher Adventure Game', 'elden-ring', 'for-honor']

for i in range(len(gamename)):
    url = "https://gabestore.ru/game/" + gamename[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    if soup.find('div', class_="b-card__price-currentprice") is not None:
        print(gamename[i] + ' ' + soup.find('div', class_="b-card__price-currentprice").text)
    else:
        print(gamename[i] + ' ' + 'Нет в наличии')