from django import urls
from django.urls import path
from .views import *
urlspatterns = [
    path('',  , name='post_list')
]