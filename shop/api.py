from django.http import JsonResponse
from .services.cart import CartService
from .services.product import ProductService
from .services.order import OrderService
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def add_to_cart(request,id):
    user_name = request.GET.get('user')
    user = User.objects.get(username = user_name)
    print("User:",user)
    count = int(request.GET.get('count'))
    print(count)
    product = ProductService.get_by_id(id)
    print("Product:",product)
    if(product != None):
        product_in_cart = CartService.add_cart_item(user,product,count)
        if(product_in_cart != None):
            print("prodcuct exists")
            return JsonResponse({"message":"Item saved."})
        else:
            return JsonResponse({"status":"error","message":"Failed to save item."},status=400)
    else:
        return JsonResponse({"status":"error","message":"Failed to save item."},status=400)

@login_required(login_url='/user/login/')
def add_to_order(request,id):
    count = int(request.GET.get('count'))
    user =  int(request.GET.get('user'))
    product = ProductService.get_by_id(id)
    if(product != None):
        product_in_order = OrderService.add_order_item(user,product,count)
        if(product_in_order != None):
            return JsonResponse({"message"})

def search_suggestions(request):
    query = request.GET.get('q')
    suggestions = ProductService.suggestions(query)
    return JsonResponse([(suggestion.id,suggestion.name,suggestion.photo.url) for suggestion in suggestions], safe=False)

def adjust_quantity(request):
    product_id = ProductService.get_by_id(int(request.GET.get('product')))
    count = int(request.GET.get('count'))
    CartService.set_quantity(User.objects.filter(id = request.GET.get('userid'))[0],product_id,count)
    return JsonResponse({"message":"successfully updated cart_item"})
