

from services import create_order
from uow_impl import SQLalchemyUnitOfWork


def test_create_order():
    uow = SQLalchemyUnitOfWork()
    create_order(1, 1, uow)

    assert True
