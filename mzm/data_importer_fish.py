# UMZM migratory bird specimens_Feb2015.xls
import sys, os, django
import xlrd
import dotenv
from django.utils import timezone
from datetime import datetime

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

    timezone.now()

    book = xlrd.open_workbook("./data_seed/UMZM migratory bird specimens_Feb2015-Converted.xls")
    sh = book.sheet_by_index(0)

    print('Start importing data...')

    print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    for r in range(sh.nrows)[2:]:
        data = sh.row(r)

        taxon = Taxon.objects.create(family=data[3].value, genus=data[5].value,
                                     specificEpithet=data[6].value, acceptedNameUsage=data[4].value)
        occurrence = Occurrence.objects.create(catalogNumber=data[7].value,
                                               sex=data[11].value, lifeStage = str(data[12].value))
        location = Location.objects.create(stateProvince=data[9].value, locality=data[10].value)

        if data[8].ctype != xlrd.XL_CELL_EMPTY:
            date = None
            if data[8].ctype == xlrd.XL_CELL_TEXT:
                dash_count = data[8].value.count('-')
                slash_count = data[8].value.count('/')
                if dash_count == 0:
                    if slash_count == 0:
                        date = datetime.strptime(data[8].value, "%Y")
                    else:
                        date = datetime.strptime(data[8].value, "%m/%d/%Y")
                elif dash_count == 1:
                    date = datetime.strptime(data[8].value, "%b-%Y")
                else:
                    date = datetime.strptime(data[8].value, "%d-%b-%Y")
            else:
                date = xlrd.xldate.xldate_as_datetime(data[8].value, 0)
            event = Event.objects.create(eventDate=timezone.make_aware(date, timezone.get_current_timezone()))
        else:
            event = None

        if data[0].ctype != xlrd.XL_CELL_EMPTY:
            identification = Identification.objects.create(identificationID=int(data[0].value))
        else:
            identification = None
        root = Root(
            eventID=event,
            locationID = location,
            identificationID = identification,
            taxonID = taxon,
            occurrenceID = occurrence,
            type = data[2].value,
            collectionName = 'fish'
        )
        root.save()
    print("all bird data imported into database.")