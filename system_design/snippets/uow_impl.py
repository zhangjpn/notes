

from abstract_uow import AbstractUnitOfWork
from abstract_repository import AbstractRepository


def default_session_factory():
    return


class SQLalchemyUnitOfWork(AbstractUnitOfWork):
    order: AbstractRepository

    def __init__(self, session_factory=default_session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        return self.session

    def __exit__(self, exc, exc_type, trackback):
        if exc:
            print(exc, exc_type, trackback)
            self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
