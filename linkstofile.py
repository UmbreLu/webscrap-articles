import requests
from bs4 import BeautifulSoup

url = 'https://adrenaline.com.br/'
links_list = []

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')

links = []

articles = []

for article in soup.find_all('article', limit=3):
	links.append(article.find('a').get('href'))

for link in links:
	req2 = requests.get(link)

	soup2 = BeautifulSoup(req2.text, 'html.parser')

	for string in soup2.find('div', class_="news__text").stripped_strings:
		with open('adrena_artigos.txt', 'a') as file:
			file.write(string)


#with open('adrenaartigos.txt', 'a') as file:
#	for link in links:
#		file.write(link + '\n')
