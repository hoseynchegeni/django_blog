from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class PostListApiView(TemplateView):
    template_name = 'home.html'