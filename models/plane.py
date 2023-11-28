from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR, FLOAT, ForeignKey
from models import Company

class Plane(Base):
    __tablename__ = "plane"
    id: Mapped[int] = mapped_column("id", INTEGER, primary_key=True, autoincrement=True, nullable=False)
    model: Mapped[str] = mapped_column("model", VARCHAR(50), nullable=False)
    coord_x: Mapped[float] = mapped_column("coord_x", FLOAT, nullable=False)
    coord_y: Mapped[float] = mapped_column("coord_y", FLOAT, nullable=False)
    coord_z: Mapped[int] = mapped_column("coord_z", INTEGER, nullable=False)
    company_id: Mapped[int] = mapped_column("company_id", INTEGER, ForeignKey(Company.id), nullable=False)