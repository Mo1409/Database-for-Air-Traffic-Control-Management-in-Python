from models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import INTEGER, VARCHAR


class Company(Base):
    __tablename__ = "company"
    id: Mapped[int] = mapped_column("id", INTEGER, primary_key=True, autoincrement=True, nullable=False)
    cnpj: Mapped[str] = mapped_column("cnpj", VARCHAR(20), nullable=False)
    company_name: Mapped[str] = mapped_column("company_name", VARCHAR(300), nullable=False)