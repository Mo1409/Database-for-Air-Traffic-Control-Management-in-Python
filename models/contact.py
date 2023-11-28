from models import Base 
from sqlalchemy.orm import mapped_column, Mapped, relationship 
from sqlalchemy import INTEGER, VARCHAR, ForeignKey 
from models import People 
from models import Company  

class Contact(Base):     
    __tablename__ = "contact"     
    id: Mapped[int] = mapped_column("id", INTEGER(), primary_key=True, nullable=True, autoincrement=False)
    people_id: Mapped[int] = mapped_column("people_id", INTEGER, ForeignKey(People.id), primary_key=False, nullable=True)     
    company_id: Mapped[int] = mapped_column("company_id", INTEGER, ForeignKey(Company.id), primary_key=False, nullable=True)
    phone: Mapped[str] = mapped_column("phone",VARCHAR(20), nullable=False)     
    email: Mapped[str] = mapped_column("email",VARCHAR(50), nullable=False)