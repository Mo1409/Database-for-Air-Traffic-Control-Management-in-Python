from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import SMALLINT, INTEGER, CHAR, DATE, BOOLEAN, DECIMAL, VARCHAR, ForeignKey
from datetime import date
from models import Plane
from models import Employee

class Maintenance(Base):
    __tablename__  = "maintenance"
    plane_id: Mapped[int] = mapped_column("plane_id", INTEGER,  ForeignKey(Plane.id), primary_key=True, nullable= False)
    employee_id: Mapped[int] = mapped_column("employee_id", INTEGER, ForeignKey(Employee.people_id), primary_key=True, nullable= False)
    maintenance_date: Mapped[date] = mapped_column("maintenance_date", DATE, nullable=False)