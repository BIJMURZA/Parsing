import requests
from bs4 import BeautifulSoup

api_key ='39864BB6D6F58565CFF414BD1280495D'

app_id = 782330

url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

params = {
    'key': api_key
}

response = requests.get(url, params=params)
data = response.json()

for i in data['applist']['apps']:
    if i['appid'] == app_id:
        game = i['name']
        print(game)
        break

url = 'https://store.steampowered.com/app/' + str(app_id)
response = requests.get(url, headers={'Accept-Language': 'ru-RU'})
soup = BeautifulSoup(response.text, "lxml")
game = soup.find('div', class_="game_description_snippet")
print(' '.join(game.text.split()))