from database import session_scope


def add_to_database(url):
    with session_scope() as session:
        session.add(url)
