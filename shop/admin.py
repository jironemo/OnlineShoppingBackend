from django.contrib import admin
from .models import Product,Category,CartProducts,Order,Cart,OrderItem
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartProducts)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)