from sqlalchemy import Column, Integer, String
from database_abstractions.database import Base


class Url(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url_string = Column(String, unique=True)
