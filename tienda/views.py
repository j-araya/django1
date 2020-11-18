from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'login/login.html')

def registro(request):
    return render(request, 'registro/registro.html')