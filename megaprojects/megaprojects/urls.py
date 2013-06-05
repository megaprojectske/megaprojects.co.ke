from django.conf.urls import patterns, include, url

from .views import FrontPageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(regex=r'^$', view=FrontPageView.as_view(),
                           name='frontpage'),

                       # Examples:
                       # url(r'^$', 'megaprojects.views.home', name='home'),
                       # url(r'^megaprojects/',
                       # include('megaprojects.foo.urls')),

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
