from typing import List
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from base import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

    addresses: Mapped[List['Address']] = relationship(
        back_populates='user', cascade='all, delete, delete-orphan'
    )
    likes: Mapped[List['Like']] = relationship(
        back_populates='user', cascade='all, delete, delete-orphan'
    )

    def __init__(self, name, password, addresses=None):
        self.name = name
        self.password = password
        self.addresses = addresses or []
