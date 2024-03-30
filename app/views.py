from django.shortcuts import render, redirect
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
    if request.method == "POST":
        id = request.POST.get("id")
        method = request.POST.get("method")
        if method == "DELETE":
            try:
                category = Category.objects.get(pk=id)
                category.delete()
            except:
                return redirect("app:index")
    return render(request, "app/index.html", {"cate": categories})


def about(request):
    return render(request, "app/about.html")


def add_category(request, id=None):
    errors = {}
    c = None
    name = ""
    if id is not None:
        try:
            c = Category.objects.get(pk=id)
            name = c.name
        except:
            return redirect("app:category_add")
    if request.method == "POST":
        method = request.POST.get("method", "POST")
        name = request.POST.get("name")
        if name == "":
            errors["name"] = "Поле наименование не может быть пустым."
        if errors:
            return render(request, "app/category_add.html", {"id": id, "name": name, "errors": errors})
        try:
            if method == "POST":
                c = Category()
                c.name = name
                c.save()
            elif method == "PUT":
                c = Category.objects.get(pk=id)
                c.name = name
                c.save()
            return redirect("app:index")
        except:
            errors["name"] = "Такая категория уже существует."
            return render(request, "app/category_add.html", {"errors": errors, "id": id, "name": name})
    return render(request, "app/category_add.html", {"id": id, "name": name})
