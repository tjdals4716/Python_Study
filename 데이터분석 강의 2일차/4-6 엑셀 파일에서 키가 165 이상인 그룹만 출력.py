import xlrd
import xlwt

workbook = xlrd.open_workbook('/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/Excel/singer.xls')
outWorkbook = xlwt.Workbook()
idx = 4 # 평균 키의 인덱스

wsheetList = workbook.sheets()
outSheet = outWorkbook.add_sheet("singer")
worksheet = wsheetList[0]
for col in range(worksheet.ncols):
    outSheet.write(0, col, worksheet.cell_value(0, col))

totalRow = 0
for worksheet in wsheetList :
    for row in range(1, worksheet.nrows) :
        height = worksheet.cell_value(row, idx)
        if int(height) >= 165 :
            totalRow += 1
            for col in range(worksheet.ncols) :
                outSheet.write(totalRow, col, worksheet.cell_value(row, col))

outWorkbook.save('/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/Excel/singer1.xls')
print("Save. OK~")