from typing import List
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from base import Base


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[Text] = mapped_column(Text)

    likes: Mapped[List['Like']] = relationship(
        back_populates='post', cascade='all, delete, delete-orphan'
    )

    def __init__(self, title, content):
        self.title = title
        self.content = content
