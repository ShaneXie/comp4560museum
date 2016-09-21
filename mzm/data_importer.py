# UMZM migratory bird specimens_Feb2015.xls
import xlrd
book = xlrd.open_workbook("./data_seed/UMZM migratory bird specimens_Feb2015.xls")
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
for rx in range(3):
    print(sh.row(rx))