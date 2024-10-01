from shop.services.cart import CartService

class UserService():
    @staticmethod
    def create_cart(user):
        cart = CartService.create_cart(user)