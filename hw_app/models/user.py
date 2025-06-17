from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing_extensions import TYPE_CHECKING

from models.base import Base

if TYPE_CHECKING:
    from models import Post


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(
        String(length=32),
        unique=True,
    )
    name: Mapped[str] = mapped_column(
        String(length=32),
        unique=False,
    )
    email: Mapped[str | None] = mapped_column(
        String(length=150),
        unique=True,
        server_default="",
        default="",
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    def __str__(self):
        return f"{self.username} ({self.email})"

    def __repr__(self):
        return str(self)
