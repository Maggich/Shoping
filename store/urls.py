from django.urls import path
from .views import product_list
from . import views


urlpatterns = [
    path('', product_list, name='product_list'),
    path('about/', views.about, name='about'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]