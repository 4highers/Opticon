from contextlib import contextmanager
from typing import Callable, Dict, Generator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from configs.envs import DATABASE_URI, DEBUG


class _Handler(object):

    def __init__(self):
        self._engine = create_engine(DATABASE_URI, echo=DEBUG)
        self._session_factory: Callable[..., Session] = sessionmaker(
            bind=self._engine,
            autoflush=True,
            autocommit=False,
            expire_on_commit=False,
            future=True)
        self.BaseModel = declarative_base(bind=self._engine)  # pylint: disable=invalid-name

    @contextmanager
    def session_scope(self) -> Generator[Session, None, None]:
        session = self._session_factory()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @property
    def metadata(self) -> MetaData:
        return self.BaseModel.metadata

    def create_all(self):
        self.metadata.create_all()

    def drop_all(self):
        self.metadata.drop_all()

    def default_table_args(self, comment: str) -> Dict[str, str]:
        return {
            'comment': comment,
            'mysql_engine': 'innodb',
            'mysql_charset': 'utf8mb4',
        }


db = _Handler()
