from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import settings

engine = create_engine(
    settings.db.url_sync,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

Session = sessionmaker(
    bind=engine,
)
