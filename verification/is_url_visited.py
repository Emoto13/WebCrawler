from database_abstractions.database import session_scope
from models.url import Url


def is_url_visited(url_string):
    with session_scope() as session:
        does_url_exist = bool(session.query(Url).filter(Url.url_string == url_string).first())
    return does_url_exist
