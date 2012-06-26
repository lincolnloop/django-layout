from django.conf.urls.defaults import patterns, url, include

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('{{ project_name }}.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
