"""mzm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mzm_api import views as api_views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$',api_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/(?P<pk>[0-9]+)/$',api_views.Occurrence_detail ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
