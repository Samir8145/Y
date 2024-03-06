from django.shortcuts import render, redirect
from .forms import  RegisterForm
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.models  import User
from .models import Customer

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        customer = Customer.objects.get(user=user)
        if user and customer:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'login': login, 'error': 'Invalid username or password'})
    return render(request, 'login.html', {'login': login})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['password_again']:
                    user = User.objects.create_user(
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password']
                    )
                    customer= Customer.objects.create(user=user)
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'register.html', {'form': form, 'error': 'Password do not match'})
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            return redirect('login')
        return render(request, 'forgot-password.html', {'error':'Hele email yoxdu'})
    return render(request, 'forgot-password.html')