from ..models import Product,Category
from .base import BaseService
from django.core.paginator import Paginator
from django.db.models import Q

class ProductService(BaseService):
    model = Product

    @staticmethod
    def save(product):
        Product.save(product)

    @staticmethod
    def top_products():
        top_products = Product.objects.all().order_by('-hitcount')[0:6]
        return top_products

    @staticmethod
    def get_by_category(category_id,page):
        category = Category.objects.filter(id=category_id)[0]
        products_by_category = Product.objects.filter(category = category)
        paginator = Paginator(products_by_category,6)
        return paginator.page(page)
    
    @staticmethod
    def get_related_products(product):
        related_products = Product.objects.filter(category=product.category).exclude(id=product.id).order_by('-hitcount')[0:3]
        return related_products
    
    @staticmethod
    def suggestions(query):
        return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))[:10]