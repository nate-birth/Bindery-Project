from django.shortcuts import render, redirect, HttpResponse
from .models import *

def store(request):
    context = {
        'products': Product.objects.filter(stock__gt=0)
    }
    return render(request, "store/store.html", context)

def productPage(request, pid):
    getProduct = Product.objects.get(id=pid)
    stockCount = []
    counter = 1
    if getProduct.stock > 10:
        for i in range(10):
            stockCount.append(counter)
            counter += 1
    else:
        for i in range(getProduct.stock):
            stockCount.append(counter)
            counter += 1

    context = {
        'product': getProduct,
        'stock': stockCount
    }
    return render(request, "store/product.html", context)

def add_to_cart(request):
    #check to see if there is an order in session
    #if no order create new order
    #else continue
    #check if orderItem is already in the order
    #if yes then increment the qty
    #else
    #create orderItem
    #add orderItem to order
    #save order in session