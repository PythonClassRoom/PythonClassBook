import requests
from bs4 import BeautifulSoup

base_url = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")

filename = input("File to save to: ")

with open(filename, 'w') as f:
    for story_heading in soup.findAll('span', {"class": "mw-headline"}):
        f.write(story_heading.text)