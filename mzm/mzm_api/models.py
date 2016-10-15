from django.db import models

    
class Identification(models.Model):
    identificationID = models.CharField(max_length=100,primary_key=True)
    #  An identifier for the Identification (the body of information associated with the assignment of a scientific name). May be a global unique identifier or an identifier specific to the data set.
    #  Didn't specify type
    identifiedBy = models.CharField(max_length=100)
    #  Didn't specify type

class Event(models.Model):
    eventID = models.CharField(max_length=255,primary_key=True)
    #  An identifier for the set of information associated with an Event (something that occurs at a place and time). May be a global unique identifier or an identifier specific to the data set.
    #  Didn't specify type
    eventDate = models.DateTimeField()
    #  Examples: "1963-03-08T14:07-0600" is 8 Mar 1963 2:07pm in the time zone six hours earlier than UTC,
    verbatimEventDate = models.CharField(max_length = 255)
    #  Examples: "1963-03-08T14:07-0600" is 8 Mar 1963 2:07pm in the time zone six hours earlier than UTC,
    habitat = models.CharField(max_length = 255)
    #  Examples: "oak savanna", "pre-cordilleran steppe"
    samplingProtocol = models.CharField(max_length = 255)
    #  Examples: "UV light trap", "mist net", "bottom trawl", "ad hoc observation",


class Location(models.Model):
    locationID = models.CharField(max_length = 255,primary_key = True)
    stateProvince = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    municipality = models.CharField(max_length = 255)
    #  Examples: "Holzminden"
    locality = models.CharField(max_length = 255)
    #  Example: "Bariloche, 25 km NNE via Ruta Nacional 40 (=Ruta 237)"
    verbatimElevation = models.CharField(max_length = 30)
    #  Example: "100-200 m".
    minimumElevationInMeters = models.CharField(max_length = 30)
    #  Example: "100".
    verbatimCoordinates = models.CharField(max_length = 255)
    #  Examples: "41 05 54S 121 05 34W", "17T 630000 4833400".
    verbatimLatitude = models.CharField(max_length = 100)
    #  Example: "41 05 54.03S".
    verbatimLongitude  = models.CharField(max_length = 100)
    #  Example: "121d 10' 34" W". 
    verbatimCoordinateSystem = models.CharField(max_length = 100)
    #  Examples: "decimal degrees", "degrees decimal minutes", "degrees minutes seconds"
    verbatimSRS = models.CharField(max_length = 100)
    #  Examples: "EPSG:4326", "WGS84", "NAD27"
    decimalLatitude = models.FloatField()
    decimalLongitude = models.FloatField()
    #  "-121.1761111"
    geodeticDatum = models.CharField(max_length = 100)
    #  Examples: "EPSG:4326", "WGS84", "NAD27", "Campo Inchauspe"
    coordinateUncertaintyInMeters = models.IntegerField()
    #  Examples: "30"

class Taxon(models.Model):
    taxonID = models.CharField(max_length=100,primary_key = True)
    scientificNameID = models.CharField(max_length = 255)
    #  Example: "urn:lsid:ipni.org:names:37829-1:1.3".
    acceptedNameUsage = models.CharField(max_length = 255)
    #  Example: "Tamias minimus" valid name for "Eutamias minimus".
    kingdom = models.CharField(max_length = 100)
    #  Examples: "Animalia", "Plantae". 
    phylum = models.CharField(max_length = 100)
    #  Examples: "Chordata" (phylum), "Bryophyta" (division). 
    Taxonclass  = models.CharField(max_length = 100)
    order = models.CharField(max_length = 100)
    family = models.CharField(max_length = 100)
    genus = models.CharField(max_length = 100)
    subgenus = models.CharField(max_length = 100)
    #  Examples: "Strobus (Pinus)", "Puma (Puma)" "Loligo (Amerigo)"
    specificEpithet = models.CharField(max_length = 100)
    #  Examples: "concolor", "gottschei"
    taxonRank = models.CharField(max_length = 100)
    #  Examples: "subspecies", "varietas", "forma"
    verbatimTaxonRank = models.CharField(max_length = 100)
    #  Examples: "Agamospecies", "sub-lesus", "prole", "apomict", "nothogrex"
    scientificNameAuthorship = models.CharField(max_length = 100)
    #  Example: "(Torr.) J.T. Howell", "(Martinovský) Tzvelev"


class Occurrence(models.Model):
    occurrenceID = models.CharField(max_length=100,primary_key=True)
    #OccurrenceType:
    #  type = models.
    bibliographicCitation = models.CharField(max_length=100)
    datasetName = models.CharField(max_length=100)
    #  Examples: "Mammals", "Hildebrandt", "eBird"
    collectionCode = models.CharField(max_length=100)
    #  Examples: "Mammals", "Hildebrandt", "eBird"

    catalogNumber = models.CharField(max_length=100)
    #  Examples: "2008.1334", "145732a", "145732"

    occurenceRemarks = models.CharField(max_length=100)
    recordNumber = models.CharField(max_length=100)
    #  Examples: "José E. Crespo", "Oliver P. Pearson | Anita K. Pearson"
    recordedBy = models.CharField(max_length=100)
     #  Examples: "José E. Crespo"
    associatedMedia = models.CharField(max_length=100)
    #  "http://204.140.246.24/Fish/Collection%20Pictures/10118-00.jpg | http://204.140.246.24/Fish/Collection%20Pictures/10118-00a.jpg"
    preparations = models.CharField(max_length=255)
    #  Examples: "fossil", "cast", "photograph", "DNA extract", "skin | "skull | skeleton",
    sex = models.CharField(max_length = 100)
    #  Examples: "female", "hermaphrodite", "8 males, 4 females".
    lifeStage = models.CharField(max_length = 100)
    #  Examples: "egg", "eft", "juvenile", "adult", "2 adults 4 juveniles"
    reproductiveCondition = models.CharField(max_length = 100)
    #  Examples" "non-reproductive", "pregnant", "in bloom", "fruit-bearing".

class root(models.Model):
    eventID = models.ForeignKey(Event)
    locationID = models.ForeignKey(Location)
    identificationID = models.ForeignKey(Identification)
    taxonID = models.ForeignKey(Taxon)
    occurrenceID = models.ForeignKey(Occurrence)
    roottype = models.CharField(max_length=40)
