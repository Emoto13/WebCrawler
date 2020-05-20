from database_abstractions.add_entry_to_db import add_entry_to_db
from database_abstractions.bootstrap import bootstrap
from models.url import Url
from utils.get_last_url_if_already_searched_for import is_the_link_already_searched_for
from utils.get_urls import get_urls_and_add_server
from verification.is_url_visited import is_url_visited


def main():
    starting_url = input("Enter url: ")
    bootstrap()
    starting_url = is_the_link_already_searched_for(starting_url)
    bfs(starting_url)


def bfs(starting_url):
    queue = [starting_url]

    while queue:
        current_url_string = queue.pop(0)
        try:
            is_url_visited(current_url_string)
            current_url = Url(url_string=current_url_string)
            add_entry_to_db(current_url)
            queue.extend(get_urls_and_add_server(current_url_string))
        except Exception as e:
            print(e)




if __name__ == '__main__':
    main()
