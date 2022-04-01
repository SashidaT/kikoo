from django.contrib import admin
from django.urls import path,include
from .views import Post_ListView

app_name = 'twitter'

urlpatterns = [
    path('', Post_ListView.as_view(), name='index'),
]