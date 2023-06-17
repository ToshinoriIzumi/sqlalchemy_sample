from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from user import User
from address import Address
from like import Like
from post import Post

engine = create_engine('sqlite:///sqlalchemy_example.db')

with Session(engine) as db:
    # Create
    izumi = User(
        'Toshinori Izumi',
        'pass1',
        [
            Address('address1@example.com'),
            Address('address2@example.com'),
        ]
    )

    db.add(izumi)
    posts = [
        Post('title1', 'content1'),
        Post('title2', 'content2'),
        Post('title3', 'content3'),
    ]

    db.add_all(posts)

    likes = [
        Like(1, 1),
        Like(1, 2),
        Like(1, 3),
    ]
    db.add_all(likes)
    db.commit()

    # relationshipのデータ取得
    users = db.query(User).all()
    for user in users:
        for address in user.addresses:
            print(address.email)

    addresses = db.query(Address).all()
    for address in addresses:
        print(address.user.name)

    users = db.query(User).all()
    for user in users:
        for like in user.likes:
            print(like.post.title)
