from django.conf import urls

import views


urlpatterns = urls.patterns(
    '',
    urls.url(r'^articles/(?P<id>[\d]+)(?:/(?P<slug>[\S]+))?/$',
             views.ArticleDetailView.as_view(), name='article_detail'),
    urls.url(r'^articles/$', views.ArticleListView.as_view(kind='a'),
             name='article_list'),
    urls.url(r'^blog/$', views.ArticleListView.as_view(kind='b'),
             name='blog_list'),
)
