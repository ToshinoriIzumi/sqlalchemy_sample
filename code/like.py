from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from base import Base
from post import Post
from user import User


class Like(Base):
    __tablename__ = 'likes'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))

    post: Mapped["Post"] = relationship(back_populates='likes')
    user: Mapped["User"] = relationship(back_populates='likes')

    def __init__(self, user_id: int, post_id: int):
        self.user_id = user_id
        self.post_id = post_id
