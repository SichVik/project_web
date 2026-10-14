from linecache import clearcache

from django.shortcuts import render


import web_projects


def index(request):
    return render(request, 'web_projects/index.html')

def about(request):
    return render(request, 'web_projects/about.html')



# Create your views here.
