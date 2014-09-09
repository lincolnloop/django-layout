from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
   # url(r'', include('{{ project_name }}.apps.')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
