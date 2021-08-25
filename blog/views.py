from django.views.generic import TemplateView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


# Create your views here.

class BasePage(ListView):
    model = Post
    template_name = 'base.html'


class HomePage(TemplateView):
    template_name = 'home.html'

class AboutPage(TemplateView):
    template_name = 'about.html'


class ServicePage(TemplateView):
    template_name = 'service.html'


class PostDetailView(DeleteView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreatView(CreateView):
    model=Post
    template_name = 'new_post.html'
    fields = ['title', 'body']
    
class BlogUpdateView(UpdateView):
    model=Post
    template_name = 'new_post.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model=Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('base')