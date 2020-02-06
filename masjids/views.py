from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from .forms import MasjidCreateForm, MasjidUpdateForm
from .models import Masjid
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone


class MasjidCreateView(CreateView):

    model = Masjid
    form_class = MasjidCreateForm
    template_name = "masjids/create.html"
    success_url = reverse_lazy("portal:home")

    def form_valid(self, form):
        messages.success(self.request, "Masjid entry has been created successfully. Thank you for your contribution.")
        return super().form_valid(form)


class MasjidUpdateView(UpdateView):

    model = Masjid
    form_class = MasjidUpdateForm
    template_name = "masjids/update.html"
    success_url = reverse_lazy("portal:home")
    slug_field = "id"
    slug_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, "Masjid times has been updated successfully. Thank you for your contribution.")
        return super().form_valid(form)
