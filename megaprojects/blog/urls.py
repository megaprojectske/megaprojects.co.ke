from django.conf.urls import patterns
from django.conf.urls import url

from .views import PostListView, PostDetailView

urlpatterns = patterns(
    '',
    url(r'^(?P<id>[\d]+)(?:/(?P<slug>[\S]+))?/$',
        PostDetailView.as_view(), name='post_detail'),
    url(r'^$', PostListView.as_view(), name='post_list'),
)
