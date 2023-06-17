from sqlalchemy import create_engine

from base import Base
from user import User
from address import Address
from like import Like
from post import Post

engine = create_engine('sqlite:///sqlalchemy_example.db', echo=True)

Base.metadata.create_all(engine)
