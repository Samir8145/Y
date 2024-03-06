from django.shortcuts import render
from .forms import ModelContact
from .models import Campaign
from shop.models import Category, Product
def home(request):
    campaign = Campaign.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'campaigns': campaign, 'category': categories})

def contact(request):
    if request.method == 'POST':
        form = ModelContact(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Yox')
            forms_errors = form.errors
            return render(request, 'contact.html', {'forms_errors': forms_errors})         
    elif request.method =='GET':
        form = ModelContact()
        return render(request, 'contact.html', {'form': form})
    return render(request, 'contact.html', {'sent': True, 'message': 'Welcome'})

def searcning(request):
    search_query = request.GET.get('search')
    down = Product.objects.filter(name__icontains=search_query)
    if down:
        return render(request, 'product.html', {'products': down} )
    else:
        return render(request, 'product.html', {'error': 'There is no such product'})