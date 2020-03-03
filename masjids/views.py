import threading

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from .forms import MasjidCreateForm, MasjidUpdateForm
from .models import Masjid, MasjidStaff
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone


class MasjidCreateView(CreateView):

    model = Masjid
    form_class = MasjidCreateForm
    template_name = "masjids/create.html"
    success_url = reverse_lazy("portal:home")

    def form_valid(self, form):
        print(form.cleaned_data)
        staff_phone = form.cleaned_data['your_contact']
        masjid = form.save()
        try:
            staff = MasjidStaff.objects.get(phone=staff_phone, masjid=masjid)
            staff.action_count += 1
            staff.save()
        except MasjidStaff.DoesNotExist:
            staff = MasjidStaff.objects.create(phone=staff_phone, masjid=masjid)
        EmailThread(masjid=masjid, staff=staff, action=1).start()
        messages.success(self.request, "Masjid entry has been created successfully. Thank you for your contribution.")
        return redirect(self.success_url)


class MasjidUpdateView(UpdateView):

    model = Masjid
    form_class = MasjidUpdateForm
    template_name = "masjids/update.html"
    success_url = reverse_lazy("portal:home")
    slug_field = "id"
    slug_url_kwarg = "id"

    def form_valid(self, form):
        print(form.cleaned_data)
        staff_phone = form.cleaned_data['your_contact']
        masjid = super().get_object()
        try:
            staff = MasjidStaff.objects.get(phone=staff_phone, masjid=masjid)
            staff.action_count += 1
            staff.save()
        except MasjidStaff.DoesNotExist:
            staff = MasjidStaff.objects.create(phone=staff_phone, masjid=masjid)
        EmailThread(masjid=masjid, staff=staff, action=2).start()
        messages.success(self.request, "Masjid times has been updated successfully. Thank you for your contribution.")
        return super().form_valid(form)


class EmailThread(threading.Thread):
    def __init__(self, masjid, staff, action):
        self.masjid = masjid
        self.action = action
        self.staff = staff
        threading.Thread.__init__(self)

    def run(self):
        if self.action == 1:
            subject = "Salahtimes : New Masjid Created"
            heading = "New Masjid has been created.\nPlease check it.\nPerson Contact : {}\n\n".format(self.staff.phone)
        else:
            subject = "Salahtimes : \"{}\" Masjid Updated".format(self.masjid.name)
            heading = "New Masjid has been updated.\nPlease check it.\nPerson Contact : {}\n\n".format(self.staff.phone)
        message = heading + self.masjid.get_email_message_details
        from_email = settings.EMAIL_HOST_USER
        recipient_list = settings.ADMIN_EMAILS
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
        return True
