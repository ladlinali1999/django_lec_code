from django.shortcuts import render, HttpResponse
from .models import Product
from django.db.models import Q
# Create your views here.

def Orm(request):
    # Product.objects.create(name='abc',age=30,salary=3.5,city='Mumbai') #This orm is used to insert data in database table
    # Product.objects.get(pk=1).delete()  #this orm is used to delete a selected data
    # Product.objects.all().delete() #this orm is used to delete all record
    # return HttpResponse("Data deleted Successfully")
    # os= Product.objects.all()
    # os= Product.objects.get(name='omkar')
    # os = Product.objects.filter(name__contains='r')   #return matching record used with conditions
    # os = Product.objects.exclude(name__contains ='om') #return record not exist om 
    # os = Product.objects.filter(age__gt=24)
    # os = Product.objects.filter(age__lt=25)
    # os = Product.objects.filter(age__lte=25)
    os = Product.objects.filter(Q(name='omkar') & Q(age=24))
    return render(request, 'orm.html', {'os':os})
  
