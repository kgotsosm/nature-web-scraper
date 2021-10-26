import requests

from bs4 import BeautifulSoup

word = input("Enter the word:\n")
url = input("Enter the inp_url:\n")
r = requests.get(url)


soup = BeautifulSoup(r.content, 'html.parser')
para = soup.find('p')

for i in para:
    if word in para.text:
        print(para.text)
