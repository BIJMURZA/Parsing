import psycopg2
import googletrans
import requests
from bs4 import BeautifulSoup
from langdetect import detect
from urllib.parse import quote

def connection_db():
    connection = psycopg2.connect(dbname='games', user='baymurzaev',
                                  password='1395', host='localhost')
    return connection.cursor()


def filling_db():
    aid = []
    cursor = connection_db()
    cursor.execute('SELECT * FROM games')
    for row in cursor.fetchall():
        aid.append(row[0])
    for i in range(len(aid)):
        print("Название игры: " + str(get_game_name(aid[i])))
        print("Описание игры: " + str(get_game_description(aid[i])))
        print("Релизная дата: " + str(get_release_date(aid[i])))
        print("Оценка игры: " + str(get_game_reviews(aid[i])))
        print(" ")


def get_game_name(aid):
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

    params = {
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    for i in data['applist']['apps']:
        if i['appid'] == aid:
            response.close()
            return i['name']


def get_game_description(aid):
    url = 'https://store.steampowered.com/app/' + str(aid)
    response = requests.get(url, headers={'Accept-Language': 'ru-RU'})
    soup = BeautifulSoup(response.text, "lxml")
    game_description = soup.find('div', class_="game_description_snippet")
    game_description = ' '.join(game_description.text.split())
    if detect(game_description) == 'en':
        return googletrans.Translator().translate(game_description,
        dest="ru").text
    else:
        return game_description


def get_release_date(aid):
    url = 'https://store.steampowered.com/app/' + str(aid)
    response = requests.get(url, headers={'Accept-Language': 'ru-RU'})
    soup = BeautifulSoup(response.text, "lxml")
    date = soup.find('div', class_='date')
    date = date.text.split()
    months = {'янв.': '01', 'фев.': '02', 'мар.': '03',
              'апр.': '04', 'май': '05', 'июн.': '06', 'июл.': '07',
              'авг.': '08', 'сен.': '09', 'окт.': '10',
              'ноя.': '11', 'дек.': '12'}
    month_index = months.get(date[1])
    date[1] = date[1].replace(date[1], month_index)
    return '/'.join(date)


def get_game_reviews(aid):
    url = 'https://store.steampowered.com/app/' + str(aid)
    response = requests.get(url, headers={'Accept-Language': 'ru-RU'})
    soup = BeautifulSoup(response.text, "lxml")
    game_review = soup.find('span', class_='game_review_summary')
    return game_review.text

api_key = "39864BB6D6F58565CFF414BD1280495D"
filling_db()
