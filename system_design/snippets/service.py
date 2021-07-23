
from order_repository import OrderRepo
from service_interface import ServiceInterface


class OrderService(ServiceInterface):

    def __init__(self, repo: OrderRepo):
        # 核心业务逻辑依赖于抽象接口
        self.repo = repo
        pass

    def serve(self):
        pass

    def create_order(self, client: int, order):
        order.client = client
        self.repo.add(order)
        self.repo.commit()

        pass

    def cancel_order(self, suk: str):

        order = self.repo.get(suk)
        order.cancel()
        self.repo.commit()

    def allocate(self):

        pass
