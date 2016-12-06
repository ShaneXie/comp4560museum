from django.http import HttpResponse
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from mzm_api.models import Identification,Event,Location,Taxon,Occurrence,Root
from mzm_api.serializers import OccurrenceSerializer,UserSerializer,RootSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
def index(request):
	return HttpResponse("<h1>You reached UofM science museum data API.</h1>")



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    serializer_class = UserSerializer


class OccurrenceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Occurrence.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = OccurrenceSerializer

class RootViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Root.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = RootSerializer
