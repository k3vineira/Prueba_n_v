from django.urls import path
from . import views, include

app_name = 'APP'

urlpatterns = [
    path('', views.index, name='index'),
    
]