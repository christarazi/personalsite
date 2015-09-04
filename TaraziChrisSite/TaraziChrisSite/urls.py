
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

# http://stackoverflow.com/a/11369944
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TaraziChrisSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', include('fortune.urls')),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fortune/', include('fortune.urls')),
)

static_view = never_cache(serve)
urlpatterns += static_view(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)
