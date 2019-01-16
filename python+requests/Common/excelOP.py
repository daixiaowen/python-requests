import xlrd
import xlwt
from xlutils.copy import copy


class OperationExcel():
    '''
    操作EXCEL用例表
    '''

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.caseFileName = file_name
            self.sheet_id = sheet_id
        else:
            self.caseFileName = '..//Cases//python接口自动化测试用例模板_张翔.xls'
            self.sheet_id = 0

        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.caseFileName)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        '''
        写入excel数据
        row,col,value
        '''
        read_data = xlrd.open_workbook(self.caseFileName)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        font = xlwt.Font()
        font.name = u'微软雅黑'
        style = xlwt.XFStyle()
        style.font = font
        if value == "pass":
            # 0 黑色
            font.colour_index = 0
            sheet_data.write(row, col, "Pass", style)
        elif value == "fail":
            # 2 红色
            font.colour_index = 2
            sheet_data.write(row, col, "Fail", style)
        else:
            sheet_data.write(row, col, value)
        write_data.save(self.caseFileName)

    # 根据对应的caseid 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols
