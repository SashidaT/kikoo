from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Post 
# Create your views here.


class Post_ListView(ListView):
    '使用するモデルを指定'
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    pagenate_by = 5
