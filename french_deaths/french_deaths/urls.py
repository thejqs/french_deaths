from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from main.views import CauseListView, CauseDetailView, CauseSearchForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^first-view/$', 'main.views.first_view'),
    url(r'^deaths-total/$', 'main.views.template_view', name='deaths'),
    url(r'^total-causes/$', 'main.views.all_deaths_view', name='all_causes'),
    url(r'^cause-list-view/', CauseListView.as_view(), name='cause_list'),
    url(r'^causes/(?P<pk>[0-9]+)/$', CauseDetailView.as_view()),
    # url(r'^CauseSearchView', CauseSearchView.as_view()),
    url(r'^cause-search/$', 'main.views.cause_search', name='cause_search'),
)