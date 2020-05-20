from sqlalchemy import Column, Integer, String
from database_abstractions.database import Base


class Server(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True)
    server_name = Column(String)
