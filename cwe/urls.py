from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
)
