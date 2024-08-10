from django.http import HttpResponse
from django.shortcuts import render



def products(request):
  producto = {"name":"cama", "price":100, "description":"cama de cama"}
  return render(request, 'products.html',{
    'producto': producto
  })

def home(request):
  return render(request, 'home.html')

def contact(request):
  return render(request, 'contact.html')

def about(request):
  return render(request, 'about.html')