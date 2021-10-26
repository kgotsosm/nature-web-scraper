import requests

from bs4 import BeautifulSoup

index = int(input())
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
h2 = soup.find_all('h2')

ans = h2[index]
print(ans.text)
