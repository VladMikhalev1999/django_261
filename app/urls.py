from django.urls import path
from .views import index, about


app_name = 'app'

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about')
]
