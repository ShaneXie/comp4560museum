from rest_framework import serializers

class OccurrenceSerializer(serializers.Serializer):
    occurrenceID = serializers.IntegerField(read_only=True)
    bibliographicCitation = serializers.CharField(required=False,max_length=100)
    datasetName = serializers.CharField(required=False,max_length=100)
    collectionCode = serializers.CharField(required=False,max_length=100)
    catalogNumber = serializers.CharField(required=False,max_length=100)
    occurenceRemarks = serializers.CharField(required=False,max_length=100)
    recordNumber = serializers.CharField(required=False,max_length=100)
    recordedBy = serializers.CharField(required=False,max_length=100)
    associatedMedia = serializers.CharField(required=False,max_length=100)
    preparations = serializers.CharField(required=False,max_length=100)
    sex = serializers.CharField(required=False,max_length=100)
    lifeStage = serializers.CharField(required=False,max_length=100)
    reproductiveCondition = serializers.CharField(required=False,max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Occurrence` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.occurrenceID = validated_data.get('occurrenceID', instance.occurrenceID)
        instance.bibliographicCitation = validated_data.get('bibliographicCitation', instance.bibliographicCitation)
        instance.datasetName = validated_data.get('datasetName', instance.datasetName)
        instance.collectionCode = validated_data.get('collectionCode', instance.collectionCode)
        instance.catalogNumber = validated_data.get('catalogNumber', instance.catalogNumber)
        instance.occurenceRemarks = validated_data.get('occurenceRemarks', instance.occurenceRemarks)
        instance.recordNumber = validated_data.get('recordNumber', instance.recordNumber)
        instance.recordedBy = validated_data.get('recordedBy', instance.recordedBy)
        instance.associatedMedia = validated_data.get('associatedMedia', instance.associatedMedia)
        instance.preparations = validated_data.get('preparations', instance.preparations)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.lifeStage = validated_data.get('lifeStage', instance.lifeStage)
        instance.reproductiveCondition = validated_data.get('reproductiveCondition', instance.reproductiveCondition)
        instance.save()
        return instance
