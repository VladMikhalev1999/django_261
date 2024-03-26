from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


# Create your views here.


def index(request):
    '''
   categories = [
       {'id': 1, 'name': 'cat 1'},
       {'id': 2, 'name': 'cat 2'},
       {'id': 3, 'name': 'cat 3'}
   ]'''
    categories = Category.objects.all().order_by("name")
    try:
        category = Category.objects.get(pk=100)
    except:
        pass
    category = Category.objects.filter(pk=100)
    return render(request, "app/index.html", {"cate": categories})


def about(request):
    return render(request, "app/about.html")
