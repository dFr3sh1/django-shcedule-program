from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'authentication/home.html')

def authentication(request):
    return render(request, 'authentication/auth.html')

def appointments(request):
    return render(request, 'authentication/appointments.html')

def historique(request):
    return render(request, 'authentication/historique.html')