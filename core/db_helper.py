from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import settings


class DBHelper:
    def __init__(self, db_url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(db_url, echo=echo)
        self.session_factory = async_sessionmaker(
            self.engine, expire_on_commit=False, autoflush=False, autocommit=False
        )


db_helper = DBHelper(settings.db_url, settings.db_echo)


async def get_db():
    session = db_helper.session_factory()
    try:
        yield session
    finally:
        session.aclose()
