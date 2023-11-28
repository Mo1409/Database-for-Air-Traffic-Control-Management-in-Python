from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import SMALLINT, INTEGER, CHAR, DATE, BOOLEAN, DECIMAL, VARCHAR
from datetime import date

class People(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column("id", INTEGER(), primary_key=True, autoincrement=True, nullable=False)
    person_name: Mapped[str] = mapped_column("person_name", VARCHAR(300), nullable=False)
    cpf: Mapped[str] = mapped_column("cpf", CHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column("rg", VARCHAR(15), nullable=False)
    birth_date: Mapped[date] = mapped_column("birth_date", DATE, nullable=False)
