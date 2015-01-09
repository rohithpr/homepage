from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('app.urls')),
    url(r'^b/', include('app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
