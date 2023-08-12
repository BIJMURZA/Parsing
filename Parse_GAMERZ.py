import requests
from bs4 import BeautifulSoup

gamename = ['mortal-kombat-11-steam', 'ad-infinitum', 'tekken-7', 'jagged-alliance-3', 'days-gone', 'mortal-kombat-1',
            'no-mans-sky', 'the-witcher-adventure-game', 'elden-ring', 'for-honor']


for i in range(len(gamename)):
    url = "https://gamerz.online/product/" + gamename[i] + "-pc"
    resourse = requests.get(url)
    if resourse.status_code != 404:
        soup = BeautifulSoup(resourse.text, 'lxml')
        if soup.find('span', class_="woocommerce-Price-amount amount") is not None:
            print(gamename[i] + ' ' + soup.find('span', class_="woocommerce-Price-amount amount").text)
    else:
        print(gamename[i] + ' ' + "Нет в наличии")