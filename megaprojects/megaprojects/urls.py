from django.conf import urls
from django.contrib import sitemaps
from django.views import generic

from articles.models import Article
from programs.models import Program
import views
import feeds

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


sm = {
    'articles': sitemaps.GenericSitemap(
        {'queryset': Article.objects.published(), 'date_field': 'pubdate'}),
    'projects': sitemaps.GenericSitemap(
        {'queryset': Program.objects.published(), 'date_field': 'created'}),
}

urlpatterns = urls.patterns(
    '',
    urls.url(r'^admin/doc/', urls.include('django.contrib.admindocs.urls')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
    urls.url(r'^ckeditor/', urls.include('ckeditor.urls')),

    urls.url(r'^$', views.FrontPageView.as_view(), name='frontpage'),
    urls.url(r"^rss/index.xml$", feeds.FrontPageFeed(), name='rss'),

    urls.url(r'^', urls.include('articles.urls')),
    urls.url(r'^projects/', urls.include('programs.urls')),
    urls.url(r'^search/', urls.include('haystack.urls'), name='search'),

    urls.url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
             {'sitemaps': sm}, name='sitemap'),
    urls.url(r'^robots\.txt$', generic.TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain')),
)


import settings.base as settings
urlpatterns += urls.patterns(
    '',
    urls.url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
             kwargs={'document_root': settings.STATIC_ROOT}),
)
