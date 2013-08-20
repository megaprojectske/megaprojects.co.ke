from django.conf.urls import patterns
from django.conf.urls import url

from .views import ProgramListView, ProgramDetailView, ProgramArchiveView, ProgramLatestView

urlpatterns = patterns(
    '',
    url(r'^(?P<id>[\d]+)/details(?:/(?P<slug>[\S]+))?/$',
        ProgramDetailView.as_view(), name='program_detail'),
    url(r'^(?P<id>[\d]+)/archive(?:/(?P<slug>[\S]+))?/$',
        ProgramArchiveView.as_view(), name='program_archive'),
    url(r'^(?P<id>[\d]+)(?:/(?P<slug>[\S]+))?/$',
        ProgramLatestView.as_view(), name='program_latest'),
    url(r'^$', ProgramListView.as_view(), name='program_list'),
)
