from django.shortcuts import render
from .forms import ModelContact
from .models import Campaign
from shop.models import Category

def home(request):
    campaign = Campaign.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'campaigns': campaign, 'category': categories})

def contact(request):
    if request.method == 'POST':
        form = ModelContact(request.POST)
        print(request.POST)
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