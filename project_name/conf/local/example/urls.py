from django.conf.urls.static import static
from django.conf import settings

from {{ project_name }}.urls import urlpatterns


if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
