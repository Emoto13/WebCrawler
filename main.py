import requests
from bs4 import BeautifulSoup
import validators

from add_to_database import add_to_database
from bootstrap import bootstrap
from url import Url
from database import session_scope


def main():
    starting_url = input("Enter url: ")
    bootstrap()
    starting_url = is_the_link_already_searched_for(starting_url)
    bfs(starting_url)


def bfs(starting_url):
    queue = [starting_url]

    while queue:
        current_url_string = queue.pop(0)
        current_url = Url(url_string=current_url_string)
        try:
            add_to_database(current_url)
            queue.extend(get_urls(current_url_string))
        except Exception:
            pass


def is_the_link_already_searched_for(starting_url):
    with session_scope() as session:
        list_of_tuple_urls = session.query(Url).with_entities(Url.url_string).all()
    urls = list(map(lambda url: url[0], list_of_tuple_urls))
    if starting_url in urls:
        return urls[-1]
    return starting_url


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
