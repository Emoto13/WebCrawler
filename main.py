import requests
from bs4 import BeautifulSoup
import validators

from add_to_database import add_to_database
from bootstrap import bootstrap
from url import Url


def main():
    starting_url = input("Enter url: ")
    bootstrap()
    queue = [starting_url]

    while queue:
        current_url_string = queue.pop(0)
        current_url = Url(url_string=current_url_string)
        add_to_database(current_url)
        try:
            queue.extend(get_urls(current_url_string))
        except Exception:
            pass


def get_urls(initial_url):
    res = requests.get(initial_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    urls = soup.find_all('a')
    reference_urls = [url.get('href') for url in urls]
    return filter_urls(reference_urls)


def filter_urls(urls):
    return list(filter(lambda url: filter_function(url), urls))


def filter_function(url):
    if url is not None and validators.url(url):
        return True
    return False


if __name__ == '__main__':
    main()
