from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from .models import Root

# Create your views here.
def index(request):
	return HttpResponse("<h1>You reached UofM science museum data API.</h1>")

def collection(request, collection_name='no_name'):
	if request.method == 'GET':
		offset = int(request.GET.get('offset', 0))
		limit = int(request.GET.get('limit', 20))

		collections = Root.objects.filter(collectionName=collection_name)[offset:offset+limit]
		col_list = []

		for co in collections:
			col = {}
			col['id'] = co.id
			col['type'] = co.type
			col['collectionName'] = co.collectionName
			print(serializers.serialize("json", [co.eventID]))
			col['event'] = json.loads(serializers.serialize("json", [co.eventID]))[0]['fields']
			col['event']['eventID'] = co.eventID.eventID
			col['location'] = json.loads(serializers.serialize("json", [co.locationID]))[0]['fields']
			col['location']['locationID'] = co.locationID.locationID
			col['identification'] = json.loads(serializers.serialize("json", [co.identificationID]))[0]['fields']
			col['identification']['identificationID'] = co.identificationID.identificationID
			col['taxon'] = json.loads(serializers.serialize("json", [co.taxonID]))[0]['fields']
			col['taxon']['taxonID'] = co.taxonID.taxonID
			col['occurrence'] = json.loads(serializers.serialize("json", [co.occurrenceID]))[0]['fields']
			col['occurrence']['occurrenceID'] = co.occurrenceID.occurrenceID

			col_list.append(col)
		return JsonResponse({'error':0, 'result':col_list})
	else:
		return JsonResponse({'error': 'wrong request method'})