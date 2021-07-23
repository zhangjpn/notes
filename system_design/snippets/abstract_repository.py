
from storage_interface import AbstractStorage


class AbstractRepository(object):

    def __init__(self, storage: AbstractStorage):
        self.storage = storage

    def get(self):
        raise NotImplementedError

    def add(self):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError
