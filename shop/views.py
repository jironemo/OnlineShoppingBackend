from django.shortcuts import render
from .services.product import ProductService
from .services.category import CategoryService
from .services.cart import CartService
from .services.order import OrderService
from .services.orderlist import OrderListService
from .services.cartitem import CartItemService
def main(request):
    top_products = ProductService.top_products()
    context = {
        'products': top_products,
        'categories': CategoryService.get_all()
    }
    return render(request,"home.html",context)

def detail(request,id):
    detail = ProductService.get_by_id(id)
    detail.hitcount += 1
    ProductService.save(detail)
    related_products = ProductService.get_related_products(detail)
    context = {
        'product':detail,
        'related_products':related_products
    }
    return render(request,"detail.html",context)


def view_by_category(request,id):
    context = {
        'products':ProductService.get_by_category(id,1),
        'category_name':CategoryService.get_name_by_id(id)
    }
    return render(request,"by_category.html",context)


def checkout(request):
    products , quantities,totals,cart = CartService.get_cart_items(request.user)
    
    context = {
        'combined_items' : zip(products,quantities,totals),
        'total' : sum(totals),
        'cart' : cart
    }
    return render(request,"checkout.html",context)

def payment(request):
    cart_id = request.GET.get('cart')
    cart = CartService.get_by_id(cart_id)
    order = OrderService.create_order(cart)
    cart_items =CartItemService.get_cart_items(cart)
    OrderListService.cartitem_to_orderlist(cart_items,order)
    cart.status = False
    cart.save()
    return render(request,"success.html")    