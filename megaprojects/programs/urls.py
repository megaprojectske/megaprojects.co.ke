from django.conf.urls import patterns
from django.conf.urls import url

from .views import ProgramListedView, ProgramArchiveView, ProgramDetailView, ProgramCurrentView

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=ProgramListedView.as_view(),
                           name="program_listed"
                       ),
                       url(
                           regex=r"^(?P<pk>\d+)/archive$",
                           view=ProgramArchiveView.as_view(),
                           name="program_archive"
                       ),
                       url(
                           regex=r"^(?P<pk>\d+)/details$",
                           view=ProgramDetailView.as_view(),
                           name="program_detail"
                       ),
                       url(
                           regex=r"^(?P<pk>\d+)/$",
                           view=ProgramCurrentView.as_view(),
                           name="program_current"
                       ),
                       )
