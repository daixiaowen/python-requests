# encoding=utf-8
# __author__=zhangxiang

import xlrd
import getcwd

casePath = getcwd.get_casePath('python接口自动化测试用例模板_张翔.xls')


def read_excel(filepath, sheetName):
    api_cases = []
    try:
        workbook = xlrd.open_workbook(filepath)
        sheet = workbook.sheet_by_name(sheetName)
        nrows = sheet.nrows
    except FileNotFoundError as e:
        print("打开用例文件异常，原因是： %s" % e)
    for i in range(1, nrows):
        api_cases.append({"case_id": sheet.cell(i, 0).value,
                          'module': sheet.cell(i, 1).value,
                          'url': sheet.cell(i, 2).value,
                          'method': sheet.cell(i, 3).value,
                          'headers': sheet.cell(i, 4).value,
                          'parameters': sheet.cell(i, 5).value,
                          'expected': sheet.cell(i, 6).value,
                          'result': sheet.cell(i, 7).value})
        case_line = api_cases[i - 1]
        print(case_line)
        return case_line


if __name__ == '__main__':
    read_excel(casePath, 'Sheet1')
