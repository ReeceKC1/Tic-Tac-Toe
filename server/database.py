from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Player(Base):
    __tablename__ = 'player'

    name = Column('name', String, primary_key=True)
    password = Column('password', String)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'password': self.password
        }

class Record(Base):
    __tablename__ = 'record'

    date_time = Column('date_time', DateTime(timezone=True), server_default=func.now(), primary_key=True)
    winner = Column('winner', String, ForeignKey('player.name'))
    loser = Column('loser', String, ForeignKey('player.name'))

    @property
    def serialize(self):
        return {
            'date_time': self.date_time,
            'winner': self.winner,
            'loser': self.loser
        }

Base.metadata.create_all(engine)