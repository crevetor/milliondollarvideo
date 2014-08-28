from django.conf.urls import patterns, url

from videoplayer import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"))
