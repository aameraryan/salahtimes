from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from masjids.models import Masjid
from django.db.models import Q
from django.shortcuts import redirect
from localities.models import City
from django.contrib import messages


def test(request):
    return render(request, "portal/test.html", {"masajid": Masjid.objects.all()})


class HomeView(TemplateView):

    template_name = "portal/home.html"

    def get_context_data(self, **kwargs):
        masajid = Masjid.objects.all().order_by("name")
        context = super().get_context_data()
        context['masajid'] = masajid
        return context


def search(request):
    if request.method == "GET":
        raw_search_query = request.GET.get("query", None)
        if raw_search_query:
            search_query = raw_search_query.lower().replace("masjid", "").strip()
            queries = search_query.split(" ")
            results = Masjid.objects.filter(Q(name__icontains=search_query) | Q(address__icontains=search_query))
            for query in queries:
                query_result = Masjid.objects.filter(Q(name__icontains=query) | Q(address__icontains=query))
                results = results.union(query_result)
            results = results.order_by("name")
            return render(request, "portal/search.html", {'masajid': results, "search_query": raw_search_query})
    return redirect("portal:home")


def areas(request):
    return render(request, "portal/areas.html", {'cities': City.objects.all()})
