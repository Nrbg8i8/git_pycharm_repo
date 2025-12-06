from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

engine = create_engine('sqlite:///booking.db', echo=True)
Session = sessionmaker(bind=engine)

def init_db():

    Base.metadata.create_all(engine)

def get_session():

    return Session()
