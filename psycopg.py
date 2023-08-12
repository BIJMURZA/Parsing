import requests

cookies = {
    'cf_clearance': '6YenUt_pzj120E72tLk0vj3QQjvNdLG3cR3N5tJrfws-1691757855-0-1-cffaf297.75aa331e.cac3e71-250.2.1691757855',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}
response = requests.get('https://steamdb.info/app/730/', cookies=cookies, headers=headers)
print(response)
