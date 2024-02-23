
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import place
def demo(request):
    obj=place.objects.all()

    return render(request, "index.html",{'result':obj})


   # name="india"
   # return  render(request,"home1.html",{'obj':name})


# def add(request):
#    x=int(request.GET["num1"])
#    y=int(request.GET["num2"])
#    res=x+y
#    return render(request,'about.html',{'result':res})

