from django.shortcuts import render
from .models import Product, Color
from django.db.models import Count, F

def shop(request):
    print(request.GET.get('home'))
    colors = Color.objects.all()
    product = Product.objects.all()
    product_count = product.count()
    lst = Product.objects.aggregate(Count('color'))
    for i in colors:
        colors_count = Product.objects.filter(color=i).count()
        colors_add = Product.objects.annotate(count=F('color')).count()
    context = {
        'products': product,
        'color':colors,
        'product_count': product_count,
        'color_count':lst.get('color__count'),
        'colors_add':colors_add
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