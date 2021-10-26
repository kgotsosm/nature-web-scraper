import requests

from bs4 import BeautifulSoup

link = input()
r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')
h1 = soup.find('h1')
print(h1.text)
