import requests
import validators
from bs4 import BeautifulSoup

from database_abstractions.add_entry_to_db import add_entry_to_db
from models.server import Server


def get_urls_and_add_server(initial_url):
    request = requests.get(initial_url)
    add_entry_to_db(Server(server_name=request.headers['Server']))
    return get_urls(request)


def get_urls(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    urls = soup.find_all('a')
    reference_urls = [url.get('href') for url in urls]
    return filter_urls(reference_urls)


def filter_urls(urls):
    return list(filter(lambda url: filter_function(url), urls))


def filter_function(url):
    if url is not None and validators.url(url):
        return True
    return False
