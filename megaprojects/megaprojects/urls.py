from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='base.html')),

                       # Examples:
                       # url(r'^$', 'megaprojects.views.home', name='home'),
                       # url(r'^megaprojects/', include('megaprojects.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^articles/', include('articles.urls')),
                       url(r'^projects/', include('programs.urls')),
                       url(r'^discover/', include('blog.urls')),
                       )

import sys
import settings.base as settings

if 'runserver' in sys.argv:
    urlpatterns += patterns('', url(r'^media/(.*)$', 'django.views.static.serve', kwargs={
                            'document_root': settings.MEDIA_ROOT}),)
