from openpyxl import load_workbook

def loadTestData(file):
    wb = load_workbook(filename='E:\\Projects\\bhAPItest\\data'+'\\'+file)
    ws =wb.get_sheet_by_name('Sheet1')
    data = []
    for row in tuple(ws.rows):
        t = []
        for cell in row:
            t.append(cell.value)
        data.append(tuple(t))
    return data

if __name__ == '__main__':
    print(loadTestData('testdata.xlsx'))