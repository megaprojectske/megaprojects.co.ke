from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import GenericSitemap
from django.views.generic import TemplateView

from articles.models import Article
from programs.models import Program
from blog.models import Post
from .views import FrontPageView
from .feeds import FrontPageFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


sitemaps = {
    'articles': GenericSitemap({'queryset': Article.objects.published(), 'date_field': 'pubdate'}),
    'projects': GenericSitemap({'queryset': Program.objects.published(), 'date_field': 'created'}),
    'discover': GenericSitemap({'queryset': Post.objects.published(), 'date_field': 'pubdate'}),
}

urlpatterns = patterns('',
                       url(regex=r'^$', view=FrontPageView.as_view(),
                           name='frontpage'),
                       url(r"^rss/index.xml$", FrontPageFeed()),

                       # Examples:
                       # url(r'^$', 'megaprojects.views.home', name='home'),
                       # url(r'^megaprojects/',
                       # include('megaprojects.foo.urls')),
                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {
                           'sitemaps': sitemaps}),
                       url(r'^robots\.txt$', TemplateView.as_view(
                           template_name='robots.txt', content_type='text/plain')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/',
                       # include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^articles/', include('articles.urls')),
                       url(r'^projects/', include('programs.urls')),
                       url(r'^discover/', include('blog.urls')),

                       url(r'^ckeditor/', include('ckeditor.urls')),
                       )

import sys
import settings.base as settings

if 'runserver' in sys.argv:
    urlpatterns += patterns('', url(r'^media/(.*)$', 'django.views.static.serve', kwargs={
                            'document_root': settings.MEDIA_ROOT}),)
