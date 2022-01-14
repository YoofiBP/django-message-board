from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/show.html'


class BlogStoreView(CreateView):
    model = Post
    fields = ['title', 'body', 'author']
    template_name = 'blog/store.html'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/store.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:index')
