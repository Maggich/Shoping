from django.shortcuts import render
from .models import Product




def product_list(request):
    products = Product.objects.all() # берём все товары
    return render(request, 'store/product_list.html', {
    'products': products
    })

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product_detail.html', {
        'product': product
    })

def about(request):
    return render(request, 'store/about.html')

