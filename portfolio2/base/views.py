from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def contact(request):
    return render(request, 'base/contact.html')