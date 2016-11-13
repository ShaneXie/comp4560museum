from rest_framework import serializers
from mzm_api.models import Identification,Event,Location,Taxon,Occurrence,Root



#ModelSerializer Type
class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ("occurrenceID","bibliographicCitation","datasetName","collectionCode","catalogNumber","occurenceRemarks","recordNumber","recordedBy","associatedMedia","preparations","sex","lifeStage","reproductiveCondition")
