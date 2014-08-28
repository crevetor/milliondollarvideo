from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mdv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^player/', include('videoplayer.urls')),
    url(r'^buy/', include('videoupload.urls')),
    url(r'^', include('videoplayer.urls')),
)
