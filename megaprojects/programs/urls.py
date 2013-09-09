from django.conf import urls

import views


urlpatterns = urls.patterns(
    '',
    urls.url(r'^(?P<id>[\d]+)/archive(?:/(?P<slug>[\S]+))?/$',
             views.ProgramArchiveView.as_view(), name='program_archive'),
    urls.url(r'^(?P<id>[\d]+)/details(?:/(?P<slug>[\S]+))?/$',
             views.ProgramDetailView.as_view(), name='program_detail'),
    urls.url(r'^(?P<id>[\d]+)(?:/(?P<slug>[\S]+))?/$',
             views.ProgramLatestView.as_view(), name='program_latest'),
    urls.url(r'^$', views.ProgramListView.as_view(), name='program_list'),
)
