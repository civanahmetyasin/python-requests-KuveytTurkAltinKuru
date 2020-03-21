import requests
from bs4 import BeautifulSoup

URL = 'https://www.kuveytturk.com.tr/finans-portali/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
veriler = soup.find(class_='finans-portali')
sinif = veriler.find_all('p')

print (sinif[6].prettify().split('\n')[1])
print (sinif[7].prettify().split('\n')[1])
