
from django.urls import path
from . import  views
import web_project

urlpatterns = [
    path('', views.index),
    path('about', views.about),

]