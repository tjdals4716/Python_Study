import xlrd

workbook = xlrd.open_workbook('/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/Excel/singer.xls')
sheetCount = workbook.nsheets

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    for row in range(worksheet.nrows) :
        for col in range(worksheet.ncols) :
            print("%s" % worksheet.cell_value(row, col), end = '\t')
        print()
    print()
