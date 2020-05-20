from database_abstractions.database import session_scope


def add_entry_to_db(entry):
    with session_scope() as session:
        session.add(entry)
