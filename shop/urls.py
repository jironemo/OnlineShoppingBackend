"""
URL configuration for OnlineShoppingBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import api

#View Endpoints (HTML Response)
urlpatterns = [
    path('', views.main),
    path('product/detail/<int:id>',views.detail),
    path('product/category/<int:id>',views.view_by_category),
    path('checkout/',views.checkout),
    path('payment/',views.payment)

]

#API Endpoints (JSON Response)
urlpatterns += [
    path('product/search/',api.search_suggestions),
    path('cart/add/<int:id>',api.add_to_cart),
    path('cart/product/adjust',api.adjust_quantity)
]