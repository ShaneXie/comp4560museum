from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from mzm_api.models import Identification,Event,Location,Taxon,Occurrence,Root
from mzm_api.serializers import OccurrenceSerializer

# Create your views here.
def index(request):
	return HttpResponse("<h1>You reached UofM science museum data API.</h1>")

@api_view(['GET', 'POST'])
def Occurrence_list(request,format=None):
    """
    展示或创建Occurrence.
    """
    if request.method == 'GET':
        snippets = Occurrence.objects.all()
        serializer = OccurrenceSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OccurrenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Occurrence_detail(request, pk,format=None):
    """
    修改或删除一个Occurrence.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
