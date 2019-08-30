import requests
from bs4 import BeautifulSoup

base_url = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")

for story_heading in soup.findAll('span', {"class": "mw-headline"}):
    print(story_heading.text)
