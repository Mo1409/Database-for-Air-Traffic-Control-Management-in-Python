from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR

class Route(Base):
    __tablename__="route"
    id: Mapped[int] = mapped_column("id", INTEGER, primary_key=True, autoincrement=True, nullable=False)
    country_departure: Mapped[str] = mapped_column("country_departure", VARCHAR(45), nullable=False)
    country_arrival: Mapped[str] = mapped_column("country_arrival", VARCHAR(45), nullable=False)
    expected_time: Mapped[int] = mapped_column("expected_time", INTEGER, nullable=False)
    city_departure: Mapped[str] = mapped_column("city_departure", VARCHAR(45), nullable=False)
    city_arrival: Mapped[str] = mapped_column("city_arrival", VARCHAR(45), nullable=False)

