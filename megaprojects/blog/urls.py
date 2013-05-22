from django.conf.urls import patterns
from django.conf.urls import url

from .views import PostListedView, PostDetailView

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=PostListedView.as_view(),
                           name="post_listed"
                       ),
                       url(
                           regex=r"^(?P<pk>\d+)/$",
                           view=PostDetailView.as_view(),
                           name="post_detail"
                       ),
                       )
