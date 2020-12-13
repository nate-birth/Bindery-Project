from django.shortcuts import render, redirect, HttpResponse

def store(request):
    return render(request, "store/store.html")
