from database_abstractions.database import engine, Base


def bootstrap():
    Base.metadata.create_all(engine)
