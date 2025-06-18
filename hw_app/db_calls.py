import asyncio
from typing import Sequence, Any, TYPE_CHECKING

from sqlalchemy import select

from models import User
from models.db import Session

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

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

