from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms
from authentication.forms import ContactUsForm
from django.core.mail import send_mail
from .models import Appointment
from django.utils import timezone
    
# def appointment_list(request):
#     #Get all appointments that are not in the past and order by start time 
#     appointments = Appointment.objects.filter(
#         start_time_gte=timezone.now()
#     ).order_by("start_time")
#     # Groupe the appointmens by day
#     appointments_by_day = {}
#     for appointment in appointments:
#         day = appointment.start_time.date()
#         if day in appointments_by_day:
#             appointments_by_day[day].append(appointment)
#         else:
#             appointments_by_day[day] = [appointment]
#     # Render the view with the available slots grouped by day
#     return render(request, "authentication/appointments.html", {"appointments_by_day": appointments_by_day})
        

def email_sent(request):
    message = 'Votre rendez vous a été bien enregistré'
    return render(request, 'authentication/confirmation.html')

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
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('accueil')
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form':form, 'message':message})  

def home(request):
    return render(request, 'authentication/home.html')

def appointments(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)    
        if form.is_valid():
            email = form.cleaned_data('email')
            time = form.cleaned_data('time')
            message = form.cleaned_data('message')
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via bYou Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@byou.xyz'],
        )
            availabilities = Appointment(
                email = email,
                time = time,
                message = message,
            )
            form.save()
        return redirect('confirmation')
    else:
        form = ContactUsForm()
    return render(request, 'authentication/appointments.html', {'form': form})

def historique(request):
    return render(request, 'authentication/historique.html')