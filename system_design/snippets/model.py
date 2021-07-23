

class Client(object):
    pass


class Order(object):

    def __init__(self, client: Client):
        self.client = client

    def cancel(self):
        pass


def create_order(order, client):
    # 这个位置写入的是核心业务逻辑，不需要考虑储存的情况
    pass
