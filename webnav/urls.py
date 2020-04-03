"""webnav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin


from django.conf.urls import url
from navigation import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^welcome/$', views.welcome),
    url(r'^index/$', views.index),
    url(r'^admin/$', views.admin),
    url(r'^$', views.login),
    url(r'^urlist/$', views.urlist),
    url(r'^userlist/$', views.userlist),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^useradd/$', views.useradd),
    url(r'^urladd/$', views.urladd),
    url(r'^userdel/$', views.userdel),
    url(r'^urldel/$', views.urldel),
    url(r'^adminchangepwd/$', views.adminchangepwd),
]
