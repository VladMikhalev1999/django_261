from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
   categories = [
       {'id': 1, 'name': 'cat 1'},
       {'id': 2, 'name': 'cat 2'},
       {'id': 3, 'name': 'cat 3'}
   ]
   return render(request, "app/index.html", {"cate": categories})


def about(request):
   return render(request, "app/about.html")
