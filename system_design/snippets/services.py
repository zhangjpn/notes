

from system_design.snippets.abstract_uow import AbstractUnitOfWork
from system_design.snippets.model import Client, Order


def create_order(order_id, client_id, uow: AbstractUnitOfWork):

    client = Client(client_id)
    with uow:
        order = Order(order_id)
        order.client = client
        uow.order.add(order)
        uow.commit()
