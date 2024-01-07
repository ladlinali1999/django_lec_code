from django.shortcuts import render
from .models import Products

# Create your views here.

def Index(request):
    # insert data in table
    Products.objects.create(pname="apple speaker",price=1500,desc='This is high quality product', quantity=5)
    return render(request, 'index.html')