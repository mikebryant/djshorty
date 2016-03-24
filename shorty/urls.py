'''Shorty URLs'''
from django.conf.urls import url

from . import views
from . import app_settings

urlpatterns = [
    url(r'^$', views.do_redirect, name='redirect_base'),
    url(r'^(?P<slug>[-_\w]+)$', views.do_redirect, name='redirect'),
]

if app_settings.ADMIN_ENABLED:
    urlpatterns = [
        url(r'^delete/$', views.delete, name='delete'),
        url(r'^admin/$', views.home, name='home'),
    ] + urlpatterns
