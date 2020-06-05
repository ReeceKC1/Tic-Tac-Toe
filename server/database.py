from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Player(Base):
    __tablename__ = 'player'

    name = Column('name', String, primary_key=True)
    password = Column('password', String)

class Record(Base):
    __tablename__ 'record'

    date_time = Column('date_time', DateTime, primary_key=True)
    winner = Column('winner', String, ForeignKey('player.name'))
    loser = Column('loser', String, ForeignKey('player.name'))

Base.metadata.create_all(engine)