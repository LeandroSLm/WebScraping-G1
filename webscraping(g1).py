import requests
from bs4 import BeautifulSoup
html = requests.get("https://g1.globo.com")
conteudo = html.content
mais_titulos = []
mais_resumos = []
site = BeautifulSoup(conteudo,'html.parser')
titulos = site.find_all('div',attrs={'class' : 'feed-post-body'})
for item in titulos:
    titulo = item.find('a',attrs={"class" : 'feed-post-link'})
    mais_titulos.append(titulo.text)
    resumo = item.find('a', attrs={"class": 'bstn-relatedtext'})
    if resumo:
        mais_resumos.append(resumo.text.strip())
    else:
        mais_resumos.append("")
    

titulo_resumo = zip(mais_titulos,mais_resumos)
for tits,resums in titulo_resumo:
    print("Título :",tits)
    print("Resumo: ", resums)