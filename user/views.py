from django.shortcuts import render

# Create your views here.

def testfunc(request):
    return render(request,'user/test.html')