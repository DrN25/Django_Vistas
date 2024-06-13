from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def anotherView(request):
    return render(request, "base.html", {})

def test1(request):
    return render(request, "Template1.html", {})

def test2(request):
    return render(request, "Template2.html", {})