from re import compile as compile_regex

from contextlib import contextmanager
from typing import Callable, Dict, Generator

from sqlalchemy import MetaData, create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, Session, declarative_base, as_declarative, declared_attr

from opticon.configs.envs import DATABASE_URI, DEBUG

_TO_SNAKE_CASE = compile_regex(r'(?<!^)(?=[A-Z])')


@as_declarative()
class _BaseModel(object):

    __comment__: str
    __extra_args__: tuple = tuple()

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return _TO_SNAKE_CASE.sub('_', cls.__name__).lower()

    @classmethod
    @declared_attr
    def __table_args__(cls):
        return (*cls.__extra_args__, {
            'comment': cls.__comment__,
            'mysql_engine': 'innodb',
            'mysql_charset': 'utf8mb4',
        })

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                comment='Auto-incremented ID.')


class _Handler(object):

    def __init__(self):
        self.engine = create_engine(DATABASE_URI, echo=DEBUG)
        self._session_factory: Callable[..., Session] = sessionmaker(
            bind=self.engine,
            autoflush=True,
            autocommit=False,
            expire_on_commit=False,
            future=True)
        self.BaseModel = declarative_base(bind=self.engine, cls=_BaseModel)  # pylint:disable=invalid-name

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
