import requests
from bs4 import BeautifulSoup
import pandas as pd

terra_url = 'https://www.terra.com.br/'
browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
page = requests.get(terra_url, headers = browsers)

resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')


noticias_main = soup.find_all('a', {'class': 'card-news__text--title main-url metric-item card-related-item'})
noticias_co_main = soup.find_all('a', {'class': 'metric-item card-news__list-item--link card-related-item'})

noticias = soup.find_all('a', {'class': 'card-news__text--title main-url'})

for i in range(len(noticias_main)):
    print("・" + noticias_main[i].text)

for i in range(len(noticias_co_main)):
    print("・" + noticias_co_main[i].text)

for i in range(len(noticias)):
    print("・" + noticias[i].text)
    