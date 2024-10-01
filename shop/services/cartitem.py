from .base import BaseService
from ..models import CartProducts
class CartItemService(BaseService):
    model = CartProducts
    
    def get_cart_items(cart):
        return CartProducts.objects.filter(cart = cart)
        