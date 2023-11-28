from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote

instance: str = f"mysql+pymysql://root:{quote('14092004')}@localhost:3306/controledetrafegofinal"

if not database_exists(instance):
    create_database(instance)


engine = create_engine(instance, echo=True)
Session = Session(bind=engine, autocommit=False, autoflush=True)