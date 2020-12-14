from django.shortcuts import render, redirect
from django.contrib import messages
from ..store.models import Product

def index(request):
    context = {
        'featured': Product.objects.get(id=4),
        'recent': Product.objects.get(id=3)
    }
    return render(request, 'bindery_app/index.html', context)

def about(request):
    return render(request, "bindery_app/about.html")
