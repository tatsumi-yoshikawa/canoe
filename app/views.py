from django.shortcuts import render

# Create your views here.


# Postscript

def base(request): 
    return render(request, 'app/base.html')


def index(request): 
    return render(request, 'app/index.html')


def detail(request): 
    return render(request, 'app/detail.html')
