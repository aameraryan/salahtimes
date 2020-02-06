from django.conf.urls import url
from . import views

app_name = "masjids"

urlpatterns = [
    url(r"^create/$", views.MasjidCreateView.as_view(), name="create"),
    url(r"^update/(?P<id>[0-9]+)$", views.MasjidUpdateView.as_view(), name="update"),
]
