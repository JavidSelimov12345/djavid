from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import  Post
# Create your views here.

class Homeview(ListView):
    model=Post
    template_name='home.html'
    context_object_name='javid'

class Dview(DetailView):
    model=Post
    template_name='detail.html'
    