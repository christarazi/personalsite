from django.conf.urls import patterns, url

from fortune import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<fortuneID>\d+)/$', views.idAphorism, name='idAphorism'),
    url(r'^short/$', views.short, name='short'),
    url(r'^startrek/$', views.startrek, name='startrek')
)