from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/$', 'main.views.first_view'),
    url(r'^template_view/$', 'main.views.template_view'),
)
