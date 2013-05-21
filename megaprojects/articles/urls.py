from django.conf.urls import patterns
from django.conf.urls import url

from .views import ArticleListedView, ArticleDetailView

urlpatterns = patterns("",
                       url(
                           regex=r"^$",
                           view=ArticleListedView.as_view(),
                           name="article_listed"
                       ),
                       url(
                           regex=r"^(?P<pk>\d+)/$",
                           view=ArticleDetailView.as_view(),
                           name="article_detail"
                       ),
                       )
