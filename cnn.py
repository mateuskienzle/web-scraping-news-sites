import requests
from bs4 import BeautifulSoup
import pandas as pd

cnn_url = 'https://www.cnnbrasil.com.br/'
browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
page = requests.get(cnn_url, headers = browsers)

resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')
noticias = soup.find_all('a')

target_class_1 = 'home__title headline__primary_title'
target_class_2 = 'home__title'
target_class_3 = 'articles__title'
target_class_4 = 'webstories_title'

news_dict_cnn = {}

for i in range(len(noticias)):
    if noticias[i].get('class') != None:
        if target_class_1 in noticias[i].get('class'):
            news_dict_cnn[noticias[i].text] = noticias[i].get('href')
    if noticias[i].h3 != None:
        if target_class_2 in noticias[i].h3.get('class'):
            news_dict_cnn[noticias[i].h3.text] = noticias[i].get('href')
    if noticias[i].h3 != None:
        if target_class_2 in noticias[i].h3.get('class'):
            news_dict_cnn[noticias[i].h3.text] = noticias[i].get('href')
    if noticias[i].h3 != None:
        if target_class_2 in noticias[i].h3.get('class'):
            news_dict_cnn[noticias[i].h3.text] = noticias[i].get('href')
