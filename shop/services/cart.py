from ..models import Cart,CartProducts
from .base import BaseService
class CartService(BaseService):
    model = Cart
    @staticmethod
    def create_cart(user):
        cart = Cart()
        cart.user = user
        try:
            cart.save()
            return cart
        except:
            print("Error here")
            return None

    @staticmethod
    def add_cart_item(user,product,count):
        cart = Cart.objects.filter(user=user)
        cart_item = None
        if cart:
            cart_item = CartProducts.objects.filter(cart=cart[0],product=product)
            if(cart_item):
                cart_item[0].quantity += count
                cart_item[0].save()
            else:
                cart_item = CartProducts()
                cart_item.cart = cart[0]
                cart_item.product = product
                cart_item.quantity = count
                cart_item.save()
        else:
            print("cart doesn't exist")
            cart = CartService.create_cart(user)
            cart_item = CartProducts()
            cart_item.cart = cart
            cart_item.product = product
            cart_item.quantity = count
            cart_item.save()
        return cart_item
    
    @staticmethod
    def set_quantity(user,prod,quantity):
        cart = Cart.objects.filter(user = user)[0]
        cart_item = CartProducts.objects.filter(product = prod,cart = cart)[0]
        cart_item.quantity = quantity
        cart_item.save()

    @staticmethod
    def get_cart_items(user):
        cart = Cart.objects.filter(user = user, status = True)[0]
        cart_items = CartProducts.objects.filter(cart = cart, status = True)
        products = []
        quantities = []
        totals = []
        for item in cart_items:
            products.append(item.product)
            quantities.append(item.quantity)
            totals.append(item.product.price * item.quantity)

        
        return products ,quantities,totals,cart