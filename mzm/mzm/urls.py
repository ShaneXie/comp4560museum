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
"""
API TABLE:
for all type list:
    api/typeName
for a single Type instance
    api/TypeName/number
"""
from django.conf.urls import url
from django.contrib import admin
from mzm_api import views as api_views
from mzm_api.views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers


Occurrence_list = OccurrenceViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
Occurrence_detail = OccurrenceViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
Root_list = RootViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
Root_detail = RootViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
Identification_list = IdentificationViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
Identification_detail = IdentificationViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
Event_list = EventViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
Event_detail = EventViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
Location_list = LocationViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
Location_detail = LocationViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
Taxon_list = TaxonViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
Taxon_detail = TaxonViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
urlpatterns = [
    url(r'^$',api_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/Occurrence/(?P<pk>[0-9]+)/$',Occurrence_detail,name="Occurrence_detail"),
    url(r'^api/Root/(?P<pk>[0-9]+)/$',Root_detail,name="Root_detail"),
    url(r'^api/Location/(?P<pk>[0-9]+)/$',Location_detail,name="Location_detail"),
    url(r'^api/Identification/(?P<pk>[0-9]+)/$',Identification_detail,name="Identification_detail"),
    url(r'^api/Event/(?P<pk>[0-9]+)/$',Event_detail,name="Event_detail"),
    url(r'^api/Taxon/(?P<pk>[0-9]+)/$',Taxon_detail,name="Taxon_detail"),
    # url(r'^adi/$',Root_list,name="Root_list"),
    url(r'^api/Occurrence$',Occurrence_list,name="Occurrence_list"),
    url(r'^api/Root$',Root_list,name="Root_list"),
    url(r'^api/Location$',Location_list,name="Location_list"),
    url(r'^api/Identification$',Identification_list,name="Identification_list"),
    url(r'^api/Event$',Event_list,name="Event_list"),
    url(r'^api/Taxon$',Taxon_list,name="Taxon_list"),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
