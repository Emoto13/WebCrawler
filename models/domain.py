from datetime import datetime

from sqlalchemy import Column, Integer, String, DATETIME
from database_abstractions.database import Base
from utils.get_domain import get_domain_from_url_string


class Domain(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True)
    domain_name = Column(String)
    visited_at = Column(DATETIME)


def create_domain(url_string=None):
    domain_name = get_domain_from_url_string(url_string)
    now = datetime.now()
    return Domain(domain_name=domain_name, visited_at=now)
