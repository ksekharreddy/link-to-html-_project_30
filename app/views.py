from django.shortcuts import render
from app.models import *

# Create your views here.

def Topic_display(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'Topic_display.html',d)

def Webpage_display(request):
    WOT=Webpage.objects.all()
    d={'topics':WOT}
    return render(request,'Webpage_display.html',d)

def AccessRecord_display(request):
    AOT=AccessRecord.objects.all()
    d={'topics':AOT}
    return render(request,'AccessRecord_display.html',d)