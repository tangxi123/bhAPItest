from openpyxl import load_workbook
import json

def loadTestData(file):
    wb = load_workbook(filename='E:\\Projects\\bhAPItest\\data'+'\\'+file)
    ws =wb.get_sheet_by_name('Sheet1')
    data = []
    for row in tuple(ws.rows):
        t = []
        for cell in row:
            t.append(cell.value)
        data.append(tuple(t))
    return tuple(data)

if __name__ == '__main__':
    #print(loadTestData('testdata.xlsx'))
    # data = {"c": 0, "b": 0, "a": 0}
    # print(type(data))
    # s = json.dumps(data)
    g = json.loads(["foo", {"bar":["baz", 'null', 1.0, 2]}])
    # print(type(s))
    print(type(g))
