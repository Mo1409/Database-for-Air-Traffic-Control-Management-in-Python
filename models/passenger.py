from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR, BOOLEAN, ForeignKey, DATE
from datetime import date
from models import People

class Passenger(Base):
    __tablename__="passengers"
    passport_num: Mapped[str] = mapped_column("passport_num", VARCHAR(30), nullable=False)
    visa: Mapped[bool] = mapped_column("visa", BOOLEAN, nullable=False)
    exp_date: Mapped[date] = mapped_column("exp_date", DATE, nullable=False)
    people_id: Mapped[int] = mapped_column("people_id", ForeignKey(People.id), primary_key=True)
