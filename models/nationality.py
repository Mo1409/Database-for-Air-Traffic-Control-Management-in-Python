from typing import List
from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR

class Nationality(Base):
    __tablename__ = "nationality"
    id: Mapped[int] = mapped_column("id", INTEGER, primary_key=True, autoincrement=True, nullable=False)
    country_name: Mapped[str] = mapped_column("person_name", VARCHAR(300), nullable=False)
    continent: Mapped[str] = mapped_column("continent", VARCHAR(50), nullable=False)