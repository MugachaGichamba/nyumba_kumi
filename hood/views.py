from django.shortcuts import render
from .models import Business, Contact, Hood
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class BusinessListView(ListView):
    model = Business


class ContactListView(ListView):
    model = Contact


class HoodListView(ListView):
    model = Hood


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['image', 'name', 'location', 'email']

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.hood_id = self.kwargs['hood_id']
        messages.success(self.request, "Business successfully added")
        return super().form_valid(form)
