import requests
from bs4 import BeautifulSoup
import pandas as pd

r7_url = 'https://www.r7.com/'
browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
page = requests.get(r7_url, headers = browsers)

resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')

noticias = soup.find_all('a')

target_class_1 = 'r7-flex-title-h4__link'
target_class_2 = 'r7-flex-title-h5__link'
target_class_3 = 'r7-flex-title-h6__link'

            
            
for i in range(len(noticias)):
    if noticias[i].get('class') != None:
        if target_class_1 in noticias[i].get('class'):
            print(noticias[i].text.split("\n")[1].strip()) 
            print(noticias[i].get('href'))
    if noticias[i].get('class') != None:
        if target_class_2 in noticias[i].get('class'):
            print(noticias[i].text.split("\n")[1].strip()) 
            print(noticias[i].get('href'))
    if noticias[i].get('class') != None:
        if target_class_3 in noticias[i].get('class'):
            print(noticias[i].text.split("\n")[1].strip()) 
            print(noticias[i].get('href'))