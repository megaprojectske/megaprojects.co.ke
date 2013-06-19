from django.conf.urls import patterns
from django.conf.urls import url

from .views import ProgramListView, ProgramArchiveView, ProgramDetailView, ProgramLatestView

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=ProgramListView.as_view(),
                           name="program_list"
                       ),
                       url(
                           regex=r"^(?P<id>[\d]+)/archive/$",
                           view=ProgramArchiveView.as_view(),
                           name="program_archive"
                       ),
                       url(
                           regex=r"^(?P<id>[\d]+)/details/$",
                           view=ProgramDetailView.as_view(),
                           name="program_detail"
                       ),
                       url(
                           regex=r"^(?P<id>[\d]+)(?:/(?P<slug>[\S]+))?/$",
                           view=ProgramLatestView.as_view(),
                           name="program_latest"
                       ),
                       )
