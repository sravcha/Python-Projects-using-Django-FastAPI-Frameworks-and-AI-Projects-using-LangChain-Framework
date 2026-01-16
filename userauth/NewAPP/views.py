from django.shortcuts import render,redirect
from .forms import UserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def homepage(request):

    return render(request, 'NewAPP/homepage.html')

# Registration Form

def register(request):

    form = UserForm();

    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my_Login")

    context = {'registerform': form}

    return render(request, 'NewAPP/register.html', context=context)

# Login Form

def my_Login(request):

    form = LoginForm();

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
    
    context = {"loginform": form}
    return render(request, 'NewAPP/login.html', context=context)

def dashboard(request):
    return render(request, 'NewAPP/dashboard.html')



















