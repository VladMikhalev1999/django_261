from django.urls import path
from .views import *


app_name = 'app'

urlpatterns = [
    path('category/', index, name='index'),
    path('about/', about, name='about'),
    path('category/add/', add_category, name='category_add'),
    path('category/<int:id>/', add_category, name='category_edit')
]
