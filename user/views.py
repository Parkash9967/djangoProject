from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('say_hello')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # user = form.cleaned_data.get('username')
                # messages.success(request, 'Account was created for'+user)
                return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('say_hello')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('say_hello')
            else:
                messages.info(request, 'username OR password is incorrect')
        context = {}
        return render(request, 'login.html', {'form': context})


def logoutUser(request):
    logout(request)
    return redirect('login')
