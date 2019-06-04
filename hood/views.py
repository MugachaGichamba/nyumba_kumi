from django.shortcuts import render
from .models import Business
from django.views.generic import CreateView, ListView, DetailView


class ProjectListView(ListView):
    model = Business

