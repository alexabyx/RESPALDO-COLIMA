from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_colima.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'inicio.views_login.login_web', name="login_web"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administracion/', include('inicio.urls', namespace="administracion")),
    )
