from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def testfunc(request):
    return render(request,'test.html')