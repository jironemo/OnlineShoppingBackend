from .base import BaseService
from ..models import Order,Cart

class OrderService(BaseService):
    model = Order

    def create_order(cart: Cart):
        order = Order()
        order.user = cart.user
        order.save()
        return order