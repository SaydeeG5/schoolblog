from django.views.generic import (
    CreateView, 
    DetailView,
    UpdateView, 
    DeleteView, 
    ListView,
)

from .models import Post 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import ( 
    LoginRequiredMixin,
    UserPassesTestMixin
)

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post 


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post 

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "active"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post 
    fields = ["title", "subtitle", "body", "active"]

    def test_func(self):
        user= self.request.user
        post = self.get_object()
        return user == post.author 

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post 
    success_url = reverse_lazy("list")

    def test_func(self):
        user= self.request.user
        post = self.get_object()
        return user == post.author 

class BlogSearchView(ListView):
    template_name = "posts/search.html"
    model = Post 

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Post.objects.filter(title__icontains=query)| Post.objects.filter(body__icontains=query)
        
        
