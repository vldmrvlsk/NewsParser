import requests
from bs4 import BeautifulSoup

url = 'https://www.interfax.ru/russia/'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
for x in headlines:
    print(x.text.strip())