from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TaraziChrisSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', include('fortune.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fortune/', include('fortune.urls')),
)
