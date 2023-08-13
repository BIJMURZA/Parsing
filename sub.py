import requests
from bs4 import BeautifulSoup
import wikipedia

api_key ='39864BB6D6F58565CFF414BD1280495D'

app_id = 730

url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

params = {
    'key': api_key
}

response = requests.get(url, params=params)
data = response.json()
game = ''
for i in data['applist']['apps']:
    if i['appid'] == app_id:
        game = i['name']
        print(game)
        break

url = 'https://store.steampowered.com/app/' + str(app_id)
response = requests.get(url, headers={'Accept-Language': 'ru-RU'})
soup = BeautifulSoup(response.text, "lxml")
game_description = soup.find('div', class_="game_description_snippet")
print(' '.join(game_description.text.split()))

game_review = soup.find('span', class_='game_review_summary positive')
print(game_review.text)

game_date = soup.find('div', class_='date')
game_date = game_date.text.split()

months = {'янв.': '01', 'фев.': '02', 'мар.': '03',
          'апр.': '04', 'май': '05', 'июн.': '06', 'июл.': '07',
          'авг.': '08', 'сен.': '09', 'окт.': '10',
          'ноб.': '11', 'дек.': '12'}

month_index = months.get(game_date[1])
game_date[1] = game_date[1].replace(game_date[1], month_index)

print('/'.join(game_date))

url = 'https://en.wikipedia.org/wiki/Counter-Strike:_Global_Offensive'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


genre_label = soup.find('th', string='Genre(s)')


genre_data = genre_label.find_next('td')


genres = [a.get_text() for a in genre_data.find_all('a')]

print(genres)  # Вывод: ['Tactical shooter', 'First-person shooter']