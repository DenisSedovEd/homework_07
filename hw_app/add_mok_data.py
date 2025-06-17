from typing import TYPE_CHECKING
from jsonplaceholder_requests import *
from models import User, Post
from models.db import Session
import requests

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

from config import settings


def fetch_json(url: str) -> Any:
    response = requests.get(url).json()
    return response


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


def main():
    users_data = fetch_json(settings.db.mok_data_from_api)

    with Session() as session:
        create_users(session, users_data)


if __name__ == "__main__":
    main()
