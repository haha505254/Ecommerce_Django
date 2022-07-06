from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Cart(request):
    return render(request,'store/cart.html')