from django.http import HttpResponse, JsonResponse
from .models import Root

# Create your views here.
def index(request):
	return HttpResponse("<h1>You reached UofM science museum data API.</h1>")

def collection(request, collection_name='no_name'):
	if request.method == 'GET':
		offset = int(request.GET.get('offset', 0))
		limit = int(request.GET.get('limit', 20))

		collections = Root.objects.filter(collectionName=collection_name)[offset:offset+limit]
		print(collections[0].eventID)
		return JsonResponse({'result': collections[0].eventID})
	else:
		return JsonResponse({'error': 'wrong request method'})