<<<<<<< HEAD
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
=======
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View

from . import forms

def signup_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form}) 

def logout_user(request):
    logout(request)
    return redirect('login')
            
class LoginPage(View):
    """Creation of a generic login view page

    Args:
        View (_type_): argument heritance from View model

    Returns:
        request of self.template_name
    """
    form_class = forms.LoginForm    
    template_name = 'authentication/login.html'
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form':form, 'message':message})  
        
    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
>>>>>>> feature/auth
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
<<<<<<< HEAD
                #return redirect('authentication/home.html')
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'                
    return render(request, 'authentication/login.html', context={'form':form, 'message':message})  

def logout_user(request):
    logout(request)
    return redirect('login')  
=======
                return redirect('accueil')
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form':form, 'message':message})  

def home(request):
    return render(request, 'authentication/home.html')
>>>>>>> feature/auth

def appointments(request):
    return render(request, 'authentication/appointments.html')

def historique(request):
    return render(request, 'authentication/historique.html')