from bs4 import BeautifulSoup
import requests

source = requests.get('https://forums.redflagdeals.com/hot-deals-f9/').text

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())




#print(soup.prettify()) this will make the code look prettier and easy to understand
#match = soup.p.text # this will filter the code according to html tags 
#find: it will get the very first html text
#find_all : it will get all the html tags mentioned
# for article in soup.find_all('div', class_ ='article'):
'''
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)
'''