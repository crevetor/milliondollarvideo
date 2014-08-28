from django.conf.urls import patterns, url

from videoupload import views

urlpatterns = patterns('',
                       url(r'(?P<where>before|after)/(?P<vidid>[0-9]+)/$', views.buy, name="buy"))
