from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.

class homepageview(TemplateView):
    template_name = "home.html"
    model = Post
    
    
