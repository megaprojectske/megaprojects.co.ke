from django.conf.urls import patterns
from django.conf.urls import url

from .views import PostListView, PostDetailView

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=PostListView.as_view(),
                           name="post_list"
                       ),
                       url(
                           regex=r"^(?P<pk>\d+)/$",
                           view=PostDetailView.as_view(),
                           name="post_detail"
                       ),
                       )
