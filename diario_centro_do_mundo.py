import requests
from bs4 import BeautifulSoup
import pandas as pd

diario_url = 'https://www.diariodocentrodomundo.com.br/'
browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
page = requests.get(diario_url, headers = browsers)

resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')

noticias_h1 = soup.find_all('h1')
noticias_h2 = soup.find_all('h2')
noticias_h3 = soup.find_all('h3')

news_class_h1 = 'mb-0'
news_class_h2 = 'card-title m-0'
news_class_h3 = 'm-0 card-title'


for i in range(len(noticias_h1)):
    print("・" + noticias_h1[i].text.strip())

for i in range(len(noticias_h2)):
    print("・" + noticias_h2[i].text.strip())

for i in range(len(noticias_h3)):
    print("・" + noticias_h3[i].text.strip())
