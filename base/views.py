from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import re
from email.utils import parseaddr
from django.conf import settings
import uuid
from django.core.mail import send_mail
import random
import string

def home(request):
    clients = Client.objects.all()
    projects = Project.objects.all()[:4]

    context = {'title':'Home','clients':clients,'projects':projects}
    return render(request,'base/index.html',context)
def about(request):
    context = {'title':'About Us'}
    return render(request,'base/about-us.html',context)
def services(request):
    context = {'title':'Our Services'}
    return render(request,'base/services.html',context)
def contact(request):
    if request.method != 'POST':
        context = {'title':'Contact Us'}
        return render(request,'base/contact-us.html',context)
    elif request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sendEmail(email,subject,message)
        messages.success(request, f"Email Send Please Wait For Our Response")
        return redirect('contact')

def work(request):
    projects = Project.objects.all()
    context = {'title':'Our Work','projects':projects}
    return render(request,'base/work.html',context)
def history(request):
    context = {'title':'History'}
    return render(request,'base/history.html',context)
def leaders(request):
    context = {'title':'Leaders'}
    return render(request,'base/leaders.html',context)
def values(request):
    context = {'title':'Values'}
    return render(request,'base/values.html',context)
def clients(request):
    clients = Client.objects.all()
    context = {'title':'Clients','clients':clients}
    return render(request,'base/clients.html',context)
def certifications(request):
    context = {'title':'Certifications'}
    return render(request,'base/certifications.html',context)
def faq(request):
    context = {'title':'FAQ'}
    return render(request,'base/faq.html',context)


def sendEmail(email,subject,message):
    # subject
    # https://select-frankly-leech.ngrok-free.app
    # message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['subhansyed000@gmail.com']
    html_message = message + f"\n {email}"
    send_mail(
        subject,
        '',  # Use an empty string for the plain text version (optional)
        email_from,
        recipient_list,
        html_message=html_message,  # Specify the HTML content
    )
