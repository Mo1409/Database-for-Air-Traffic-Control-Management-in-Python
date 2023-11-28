from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, DATETIME, BOOLEAN, CHAR, ForeignKey, VARCHAR, DATE, DateTime
from datetime import datetime
from datetime import date
from models import Route, Plane, Company

class Trip(Base):
    __tablename__="trip"
    id: Mapped[int] = mapped_column("id", INTEGER, primary_key=True, autoincrement=True, nullable=False)
    scheduled: Mapped[date] = mapped_column("scheduled", DATETIME, nullable=False)
    delay: Mapped[bool] = mapped_column("delay", BOOLEAN, nullable=False) 
    trip_status: Mapped[str] = mapped_column("trip_status", VARCHAR(10), nullable=False) 
    gate: Mapped[str] = mapped_column("gate", CHAR(3), nullable=False)
    route_id: Mapped[int] = mapped_column("route_id", INTEGER, ForeignKey(Route.id), nullable=False)
    plane_id: Mapped[int] = mapped_column("plane_id", INTEGER, ForeignKey(Plane.id), nullable=False)
    company_id: Mapped[int] = mapped_column("company_id", INTEGER, ForeignKey(Company.id), nullable=False)




    