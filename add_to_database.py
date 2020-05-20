from database import session_scope
from url import Url


def add_to_database(url):
    # adds to db if entry doesn't exist already
    with session_scope() as session:
        if not session.query(Url).filter_by(url_string=url.url_string).first():
            session.add(url)
