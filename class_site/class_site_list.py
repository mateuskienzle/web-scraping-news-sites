import requests
from bs4 import BeautifulSoup

class Site:
    def __init__ (self, opcao:str):
        self.opcao = opcao

    def update_news(self):
        if self.opcao.lower() == 'veja':
            url = 'https://veja.abril.com.br/'
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(url, headers = browsers)

            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')

            noticias = soup.find_all('a')
            target_class_1 = 'related-article'
            target_class_2 = 'title'

            news_list_veja = []

            for i in range(len(noticias)):
                if noticias[i].get('class') != None:
                    if target_class_1 in noticias[i].get('class'):
                        news_list_veja.append([noticias[i].text, noticias[i].get('href')])
                if noticias[i].h2 != None:
                    if target_class_2 in noticias[i].h2.get('class'):
                        news_list_veja.append([noticias[i].h2.text, noticias[i].get('href')])
                if noticias[i].h3 != None:
                    if target_class_2 in noticias[i].h3.get('class'):
                        news_list_veja.append([noticias[i].h3.text, noticias[i].get('href')])
                if noticias[i].h4 != None:
                    if target_class_2 in noticias[i].h4.get('class'):
                        news_list_veja.append([noticias[i].h4.text, noticias[i].get('href')])

            self.news = news_list_veja

        if self.opcao.lower() == 'r7':
            url = 'https://www.r7.com/'
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(url, headers = browsers)

            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')

            noticias = soup.find_all('a')
            target_class_1 = 'r7-flex-title-h1__link'
            target_class_2 = 'r7-flex-bullet-h1__link'
            target_class_3 = 'r7-flex-title-h4__link'
            target_class_4 = 'r7-flex-title-h5__link'
            target_class_5 = 'r7-flex-title-h6__link'

            news_list_r7 = []        
                        
            for i in range(len(noticias)):
                if noticias[i].get('class') != None:
                    if target_class_1 in noticias[i].get('class'):
                        news_list_r7.append([noticias[i].text.split("\n")[1].strip(), noticias[i].get('href')])
                if noticias[i].get('class') != None:
                    if target_class_2 in noticias[i].get('class'):
                        news_list_r7.append([noticias[i].text.split("\n")[1].strip(), noticias[i].get('href')])
                if noticias[i].get('class') != None:
                    if target_class_3 in noticias[i].get('class'):
                        news_list_r7.append([noticias[i].text.split("\n")[1].strip(), noticias[i].get('href')])
                if noticias[i].get('class') != None:
                    if target_class_4 in noticias[i].get('class'):
                        news_list_r7.append([noticias[i].text.split("\n")[1].strip(), noticias[i].get('href')])
                if noticias[i].get('class') != None:
                    if target_class_5 in noticias[i].get('class'):
                        news_list_r7.append([noticias[i].text.split("\n")[1].strip(), noticias[i].get('href')])

            self.news = news_list_r7

        

