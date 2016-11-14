from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from mzm_api.models import Identification,Event,Location,Taxon,Occurrence,Root
from mzm_api.serializers import OccurrenceSerializer,UserSerializer
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
    serializer_class = UserSerializer


class OccurrenceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    
