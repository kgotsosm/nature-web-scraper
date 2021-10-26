import requests

from bs4 import BeautifulSoup

act = int(input()) - 1
url = input()
r = requests.get(url)
label = []

soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')

for i in a:
    label.append(i.get('href'))

print(label[act])
