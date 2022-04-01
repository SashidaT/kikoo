from django.contrib import admin
from django.urls import path
from .views import testfunc

app_name = 'user'

urlpatterns = [
    path('test/',testfunc),
]