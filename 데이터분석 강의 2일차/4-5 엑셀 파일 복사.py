import xlrd
import xlwt

workbook = xlrd.open_workbook('/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/Excel/singer.xls')
outWorkbook = xlwt.Workbook()

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    outSheet = outWorkbook.add_sheet(worksheet.name)
    for row in range(worksheet.nrows) :
        for col in range(worksheet.ncols) :
            outSheet.write(row, col, worksheet.cell_value(row, col))

outWorkbook.save('/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/Excel/singer1.xls')
print("Save. OK~")