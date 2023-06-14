class Order:
    def __init__(self, id_: int, name_: str, price_: int):
        self.id = id_
        self.name = name_
        self.price = price_


class Manager:
    def __init__(self):
        self.orders = {}

    def add_order(self, order: str):
        if order.id in self.orders:
            self.orders[order.id] += 1
        else:
            self.orders[order.id] = 1

    def remove_order(self, order_id: int):
        if order_id in self.orders:
            if self.orders[order_id] > 1:
                self.orders[order_id] -= 1
            else:
                del self.orders[order_id]

    def display_order(self):
        for order_id, quantity in self.orders.items():
            print(f'order id: {order_id}, quantity: {quantity}')


order1 = Order(1, "Product 1", 10.99)
order2 = Order(2, "Product 2", 19.37)
order3 = Order(3, "Product 3", 5.69)

manager = Manager()

manager.add_order(order1)
manager.add_order(order2)
manager.add_order(order2)
manager.add_order(order3)

manager.display_order()