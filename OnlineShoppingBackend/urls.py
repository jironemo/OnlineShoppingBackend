from django.contrib import admin
from django.urls import path,include
from pictures.conf import get_settings
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact_us.html'), name='contact_us'),
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('shop/',include('shop.urls')),
    path('user/',include('user.urls')), 
]
