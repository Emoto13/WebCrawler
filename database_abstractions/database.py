import threading
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sites.db')
Base = declarative_base()
Session = sessionmaker(bind=engine, expire_on_commit=False)
lock = threading.Lock()


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    lock.acquire()
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
        lock.release()
