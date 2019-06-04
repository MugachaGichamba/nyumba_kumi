from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from .models import Post
from django.contrib import messages
# Create your views here.


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post successfully uploaded")
        return super().form_valid(form)


class PostListView(ListView):
    model = Post

