from rest_framework import serializers
from mzm_api.models import Identification,Event,Location,Taxon,Occurrence,Root

#processhighlighted
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

#import auth User
from django.contrib.auth.models import User


#ModelSerializer Type
class OccurrenceSerializer(serializers.ModelSerializer):
    # owner = User.ForeignKey('auth.User', related_name='Occurrence')
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlighted = models.TextField()
    # highlight = serializers.HyperlinkedIdentityField(view_name='Occurrence-highlight', format='html')

    class Meta:
        model = Occurrence
        fields = ("occurrenceID","bibliographicCitation","datasetName",
        "collectionCode","catalogNumber","occurenceRemarks",
        "recordNumber","recordedBy","associatedMedia","preparations",
        "sex","lifeStage","reproductiveCondition","owner")

class RootSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Root
        fields = ("eventID","locationID","identificationID","taxonID","occurrenceID")
class EventSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Event
        fields = ("eventID","eventDate","verbatimEventDate","habitat","samplingProtocol")
class LocationSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Location
        fields = (
            "locationID","stateProvince","country","municipality",
            "locality","verbatimElevation","minimumElevationInMeters",
            "verbatimCoordinates","verbatimLatitude","verbatimLongitude",
            "verbatimCoordinateSystem","verbatimSRS","decimalLatitude",
            "decimalLongitude","geodeticDatum","coordinateUncertaintyInMeters"
        )

class IdentificationSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Identification
        fields = ("identificationID","identifiedBy")
class TaxonSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Taxon
        fields = ("taxonID","scientificNameID","kingdom","phylum","taxon_class",
        "order","family","genus","subgenus","specificEpithet","taxonRank",
        "verbatimTaxonRank","scientificNameAuthorship")


# class UserSerializer(serializers.ModelSerializer):
#     Occurrence = serializers.PrimaryKeyRelatedField(many=True, queryset=Occurrence.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'Occurrence')
