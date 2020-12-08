from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from datetime import datetime
Base = declarative_base()

class Album(Base):
    __tablename__ = 'Albums'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String)
    description = Column(String)
    owner = Column(String)

    def __init__(self, name, desc, owmer):
        self.name = name
        self.description = desc
        self.owner = owmer
        self.date = datetime.today()

class Photo(Base):
    __tablename__ = 'Photos'

    name = Column(String, primary_key=True)
    description = Column(String)
    albumid = Column(Integer, ForeignKey('Albums.id'))

    def __init__(self, name, desc, albId):
        self.name = name
        self.description = desc
        self.albumid = albId