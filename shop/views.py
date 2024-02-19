from django.shortcuts import render
from .models import Product

def shop(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(request, 'shop.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    sizes = product.size.all()
    colors = product.color.all()
    context = {
        'product': product,
        'colors': colors,
        'sizes': sizes
    }
    return render(request, 'product-detail.html', context)