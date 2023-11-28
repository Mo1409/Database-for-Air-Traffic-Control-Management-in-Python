from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR, ForeignKey
from models import People
from models import Base

class Employee(Base):
    __tablename__ = "employee"
    cnh: Mapped[str] = mapped_column ("cnh", VARCHAR(15), nullable=False, primary_key=True)
    thefunction: Mapped[str] = mapped_column("thefunction", VARCHAR(20), nullable=False)
    people_id: Mapped[int] = mapped_column("people_id", INTEGER, ForeignKey(People.id), nullable=False)
    