from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey
from models import People
from models import Nationality

class people_has_nacionality(Base):
    __tablename__ = "people_has_nacionality"
    people_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(People.id), primary_key=True)
    nationality_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Nationality.id), primary_key=True)