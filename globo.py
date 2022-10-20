import requests
from bs4 import BeautifulSoup
import pandas as pd

globo_url = 'https://www.globo.com/'
browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
page = requests.get(globo_url, headers = browsers)

resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')
noticias = soup.find_all('h2', {'class': 'post__title'})

for i in range(len(noticias)):
    print("・" + noticias[i].text)