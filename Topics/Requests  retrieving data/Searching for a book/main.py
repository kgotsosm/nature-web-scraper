import requests


def do_search(bookstore_url, params):
    r = requests.get(bookstore_url, params=params)
    return r
