from django.conf.urls import patterns
from django.conf.urls import url

from .views import ArticleListView, ArticleDetailView

urlpatterns = patterns(
    '',
    url(r'^(?P<id>[\d]+)(?:/(?P<slug>[\S]+))?/$',
        ArticleDetailView.as_view(), name='article_detail'),
    url(r'^$', ArticleListView.as_view(), name='article_list'),
)
