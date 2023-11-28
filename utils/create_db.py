from models import *
from services.database import engine

def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
