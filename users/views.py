from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Successfully created user")
            return redirect('/')
        else:
            messages.info(request, "Invalid details")
            return redirect('register')
    
    return render(request, 'register.html', {'form', form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user in None:
            return redirect('login')
        else:
            return redirect('/')
        
    return render(request, 'login.html')