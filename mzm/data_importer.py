# UMZM migratory bird specimens_Feb2015.xls
import sys, os, django
import xlrd
import dotenv

def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return -1

if __name__ == '__main__':
    dotenv.read_dotenv()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mzm.settings")
    django.setup()

    from mzm_api.models import Taxon, Occurrence, Location, Event, Root, Identification
    # if len(sys.argv) < 3:
    #     sys.exit('Usage: %s database-name file-name' % sys.argv[0])

    # if not os.path.exists(sys.argv[2]):
    #     sys.exit('ERROR: file %s was not found!' % sys.argv[1])

    book = xlrd.open_workbook("./data_seed/UMZM migratory bird specimens_Feb2015.xls")
    sh = book.sheet_by_index(0)
    print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    for r in range(sh.nrows)[2:]:
        data = sh.row(r)
        print(r)
        # print(xlrd.xldate.xldate_as_datetime(data[8].value, 0))
        taxon = Taxon.objects.create(family=data[3].value, genus=data[5].value,
                                     specificEpithet=data[6].value, acceptedNameUsage=data[4].value)
        occurrence = Occurrence.objects.create(catalogNumber=data[7].value,
                                               sex=data[11].value, lifeStage = str(data[12].value))
        location = Location.objects.create(stateProvince=data[9].value, locality=data[10].value)
        event = Event.objects.create(eventDate=xlrd.xldate.xldate_as_datetime(data[8].value, 1))
        identification = Identification.objects.create(identificationID=int(data[0].value))
        root = Root(
            eventID=event,
            locationID = location,
            identificationID = identification,
            taxonID = taxon,
            occurrenceID = occurrence,
            type = data[2].value
        )
        root.save()
    print("data saved to database.")