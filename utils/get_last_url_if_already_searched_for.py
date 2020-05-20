from database_abstractions.database import session_scope
from models.url import Url


def is_the_link_already_searched_for(starting_url):
    with session_scope() as session:
        list_of_tuple_urls = session.query(Url).with_entities(Url.url_string).all()

    urls = list(map(lambda url: url[0], list_of_tuple_urls))

    if starting_url in urls:
        return urls[-1]
    return starting_url
