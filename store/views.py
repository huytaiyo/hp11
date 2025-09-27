from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html',context)

