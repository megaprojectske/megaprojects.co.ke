from django.conf.urls import patterns
from django.conf.urls import url

from .views import ArticleListView, ArticleDetailView

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=ArticleListView.as_view(),
                           name="article_list"
                       ),
                       url(
                           regex=r"^(?P<pk>\d+)/$",
                           view=ArticleDetailView.as_view(),
                           name="article_detail"
                       ),
                       )
