import requests
from bs4 import BeautifulSoup

def get_price(game):
    for i in range(len(game)):
        url = 'https://gameray.ru/' + game[i] + '/'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        if soup.find('a', class_='ec-register-buy buy-button') is not None:
            print(game[i], soup.find('span', itemprop="price").text + "₽")
        elif soup.find('a', class_='ec-register-buy buy-button preorder') is not None:
            print(game[i], soup.find('span', itemprop="price").text + "₽")
        else:
            print(game[i], "Нет в наличии")


gamename = ['mortal-kombat-11', 'ad-infinitum', 'tekken-7', 'jagged-alliance-3', 'days-gone', 'mortal-kombat-1',
            'no-man-s-sky']
get_price(gamename)



