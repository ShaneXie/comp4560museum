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

    from mzm_api.models import Bird
    # if len(sys.argv) < 3:
    #     sys.exit('Usage: %s database-name file-name' % sys.argv[0])

    # if not os.path.exists(sys.argv[2]):
    #     sys.exit('ERROR: file %s was not found!' % sys.argv[1])

    book = xlrd.open_workbook("./data_seed/UMZM migratory bird specimens_Feb2015.xls")
    sh = book.sheet_by_index(0)
    print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    for r in range(sh.nrows)[1:]:
        data = sh.row(r)
        print(r)
        # print(xlrd.xldate.xldate_as_datetime(data[8].value, 0))
        bird = Bird(
            bid = int(data[0].value),
            umzm = int(data[1].value),
            type = data[2].value,
            family = data[3].value,
            common_name = data[4].value,
            genus = data[5].value,
            species = data[6].value,
            aou = float(data[7].value),
            date = xlrd.xldate.xldate_as_datetime(data[8].value, 0),
            prov = data[9].value,
            city = data[10].value,
            sex = data[11].value,
            fate = str(data[12].value),
            mount = intTryParse(data[13].value),
            nest = intTryParse(data[14].value),
            egg = intTryParse(data[15].value),
            model = intTryParse(data[16].value),
            burdock = intTryParse(data[17].value),
            wings = intTryParse(data[18].value)
        )
        bird.save()
    print("data saved to database.")