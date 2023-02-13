from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from . import forms


def home(request):
    return render(request, 'authentication/home.html')

def authentication(request):
    return render(request, 'authentication/auth.html')

def login_page(request):
    #To call our form and post it with  the request method
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                #return redirect('authentication/home.html')
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'                
    return render(request, 'authentication/login.html', context={'form':form, 'message':message})  

def logout_user(request):
    logout(request)
    return redirect('login')  

def appointments(request):
    return render(request, 'authentication/appointments.html')

def historique(request):
    return render(request, 'authentication/historique.html')