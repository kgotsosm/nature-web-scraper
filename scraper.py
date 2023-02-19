import string
import os
import requests
from bs4 import BeautifulSoup

# Set up soup and requests
num_pages = int(input("How many pages would you like to parse?\n"))
category = input("Which category do you want to look at?\n")
current_directory = os.getcwd()

try:
    for page in range(1, num_pages + 1):
        current_page = str(page)
        url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={current_page}'
        r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        os.mkdir(f'Page_{current_page}')  # Create new directory with page number as name
        os.chdir(f'Page_{current_page}')

        soup = BeautifulSoup(r.content, 'html.parser')

        for article in soup.find_all('article'):
            cat_text = article.find('span', {'class': "c-meta__type"})

            # Find user defined articles
            if cat_text.text == category:
                rel_link = article.find('a', {'data-track-action': 'view article'})['href']
                abs_link = 'https://nature.com' + rel_link
                article_title = article.h3.text
                r2 = requests.get(abs_link)
                soup_2 = BeautifulSoup(r2.content, 'html.parser')

                # delete punctuation and replace spaces with "_"
                trans_table = str.maketrans(" ", "_", string.punctuation)
                article_title = article_title.translate(trans_table)
                article_title = article_title.replace(" ", "_")
                article_title = article_title.strip('\n')

                # find article body

                article_body = soup_2.find('div', class_='c-article-body u-clearfix')

                if article_body:
                    body = article_body.text.strip()
                else:
                    article_body = soup_2.find('div', class_="c-article-section")
                    body = article_body.text.strip()

                with open(f'{article_title}.txt', 'wb') as file:
                    file.write(body.encode('UTF-8'))
                    file.close()

        os.chdir(current_directory)

    print("Saved all articles")

except AttributeError:
    print('Invalid entry!')
