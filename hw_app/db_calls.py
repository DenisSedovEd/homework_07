import asyncio
from typing import Sequence, Any, TYPE_CHECKING

from sqlalchemy import select

from models import User, Post
from models.db import Session

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

import requests


def create_users(
    session: Session,
    users: list[dict],
) -> list[User]:
    result = []
    for user in users:
        user_for_add = User(
            id=user["id"],
            username=user["username"],
            name=user["name"],
            email=user["email"],
        )

        session.add(user_for_add)
        session.commit()
        result.append(user_for_add)
    return result


# async def crete_posts(
#     session: Session,
#     posts: list[dict],
# ) -> list[Post]:
#     result = []
#     for post in posts:
#         session.add(
#             Post(
#                 id=post["id"],
#                 title=post["title"],
#                 body=post["body"],
#                 user_id=post["userId"],
#             )
#         )
#         await session.commit()
#         result.append(Post())
#     return result


def get_users(
    session: Session,
) -> Sequence[User]:
    statement = select(User).order_by(User.id)
    result = session.execute(statement)
    return result.scalars().all()

def get_user_by_id(
        session: Session,
        user_id: int,
) -> User:
    stmt = select(User).where(User.id == user_id)
    result = session.execute(stmt)
    return result.scalars().first()

def create_user(
        session: Session,
        user: User
) -> User:
    session.add(user)
    session.commit()
    return user


# async def get_all_post_for_user(
#     session: Session,
#     user: User,
# ) -> Sequence[Post]:
#     """
#     Func for chek db.
#     :param session: async session
#     :param user: User
#     :return: All posts for User
#     """
#     statement = select(Post).where(Post.user_id == user.id)
#     result = await session.scalars(statement)
#     return result.all()


def main():
    pass
    # with Session() as session:
    # create_posts(session, posts_data)
    #     user_by_id = await get_user(session, 1)
    #     result = await get_all_post_for_user(session, user_by_id)
    #
    # print(result)


if __name__ == "__main__":
    main()
