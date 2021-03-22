from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('order-create', views.order_create, name='order-create'),
    
]