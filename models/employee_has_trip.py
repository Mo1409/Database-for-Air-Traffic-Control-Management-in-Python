from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR, ForeignKey
from models import Trip
from models import Employee

class employee_has_trip(Base):
    __tablename__ = "employee_has_trip"
    trip_id: Mapped[int] = mapped_column("trip_id", INTEGER, ForeignKey(Trip.id), primary_key=True, nullable=False)
    people_id: Mapped[int] = mapped_column("people_id",INTEGER, ForeignKey(Employee.people_id), primary_key=True, nullable=False)