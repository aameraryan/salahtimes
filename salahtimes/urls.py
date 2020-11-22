from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^", include("portal.urls", namespace="portal")),
    url(r"^suggestions/", include("suggestions.urls", namespace="suggestions")),
    url(r"^masjids/", include("masjids.urls", namespace="masjids")),
    url(r'^sw.js', (TemplateView.as_view(template_name="sw.js", content_type='application/javascript', )), name='sw.js'),

]
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
