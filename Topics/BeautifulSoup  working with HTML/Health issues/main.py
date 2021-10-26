import requests
from bs4 import BeautifulSoup

url = input()
r = requests.get(url)

result = []
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')

for i in a:
    if i.get('aria-label') and 'entity' or 'topics' in i:
        if i.get('aria-label').startswith('S') and len(i.get('aria-label')) > 1:
            result.append(i.get('aria-label'))

print(result)
