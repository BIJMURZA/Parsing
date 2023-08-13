import psycopg2
import requests
from bs4 import BeautifulSoup


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
    print(url)
    return game_description.text


api_key = '39864BB6D6F58565CFF414BD1280495D'
filling_db()
