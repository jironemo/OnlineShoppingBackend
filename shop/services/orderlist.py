from typing import List
from .base import BaseService
from ..models import CartProducts,OrderItem
class OrderListService(BaseService):
    def cartitem_to_orderlist(cart_items,order):
        for cart_item in cart_items:
            print(cart_item)
            order_item = OrderItem()
            order_item.order = order
            order_item.product = cart_item.product
            order_item.quantity = cart_item.quantity
            order_item.status = 'pending'
            order_item.save()

