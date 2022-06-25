from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import blog 
class blogcreative (PostListview):
    model=post
class blogcreative (PostCreateview):
    model=post
    fields= "__all__"
    success_url  = reverse_lazy("blog:all")
class blogcreative (PostDetailView):
    model=post
class blogcreative (PostUpdateView):
    model=post
    fields= "__all__"
    success_url  = reverse_lazy("blog:all")
class blogcreative (PostDeleteView):
    model=post
    fields= "__all__"
    success_url  = reverse_lazy("blog:all")
    