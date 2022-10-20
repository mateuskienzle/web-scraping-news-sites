import requests
from bs4 import BeautifulSoup

veja_url = 'https://veja.abril.com.br/'
browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
page = requests.get(veja_url, headers = browsers)

resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')

noticias = soup.find_all('a')

def news(noticias):
    news_dict = {}
    for i in range(len(noticias)):
        if noticias[i].get('class') != None:
            if 'related-article' in noticias[i].get('class'):
                news_dict[noticias[i].text] = noticias[i].get('href')
        if noticias[i].h2 != None:
            if 'title' in noticias[i].h2.get('class'):
                news_dict[noticias[i].h2.text] = noticias[i].get('href')
        if noticias[i].h3 != None:
            if 'title' in noticias[i].h3.get('class'):
                news_dict[noticias[i].h3.text] = noticias[i].get('href')
        if noticias[i].h4 != None:
            if 'title' in noticias[i].h4.get('class'):
                news_dict[noticias[i].h4.text] = noticias[i].get('href')
    return news_dict

news(noticias)