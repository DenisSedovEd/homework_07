from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing_extensions import TYPE_CHECKING

from models.base import Base

if TYPE_CHECKING:
    from models import User


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(
        String(length=120),
        index=True,
        unique=True,
        default="",
        server_default="",
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    user: Mapped["User"] = relationship(
        back_populates="posts",
    )

    def __str__(self):
        return f"{self.title} ({self.user_id})"

    def __repr__(self):
        return str(self)
