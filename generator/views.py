from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        char.extend(list('!@#$%^&*-_~'))
    if request.GET.get('number'):
        char.extend(list('0123456789'))

    length=int(request.GET.get('length'))

    genpass=''
    for x in range(length):
        genpass+=random.choice(char)

    return render(request,'generator/password.html',{'password':genpass})
