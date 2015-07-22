from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from main.views import CauseListView, CauseDetailView, CauseSearchForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/$', 'main.views.first_view'),
    url(r'^template_view/$', 'main.views.template_view'),
    url(r'^all_deaths/$', 'main.views.all_deaths_view'),
    url(r'^cause_list_view/', CauseListView.as_view()),
    url(r'^causes/(?P<pk>[0-9]+)/$', CauseDetailView.as_view()),
    # url(r'^CauseSearchView', CauseSearchView.as_view()),
    url(r'^cause_search/$', 'main.views.cause_search'),
)