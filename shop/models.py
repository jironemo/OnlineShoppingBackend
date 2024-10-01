from django.db import models
from pictures.models import PictureField
from django.contrib.auth.models import User

width_field = models.PositiveIntegerField(default=400)
height_field = models.PositiveIntegerField(default=400)
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True,editable=False)
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    picture = PictureField(upload_to="static/category",blank=True)
   

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=False,default=0.00)
    photo = PictureField(upload_to="static/previews",blank=True)
    hitcount = models.IntegerField(blank=False,default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.name

class Cart(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True)
    quantity = models.IntegerField(blank=False,default=1)
    status = models.BooleanField(blank=False,default=True)
    
class Order(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

class OrderItem(BaseModel):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True)
    quantity = models.IntegerField(blank=False,default=1)
    status = models.TextField(blank=False,default='pending')
