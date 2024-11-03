from xlrd import open_workbook


def read_locator(sheetname):
    data={}
    we=open_workbook("objects.xls")
    wb=we.sheet_by_name(sheetname)
    used_rows=wb.nrows
    for i  in range(1,used_rows):
        rows=wb.row_values(i)
        data[rows[0]] =(rows[1],rows[2])
    return data


def read_headers(testcase,sheetname):
    we=open_workbook("testdata.xls")
    wb=we.sheet_by_name(sheetname)
    used_rows=wb.nrows
    for i  in range(0,used_rows):
        rows=wb.row_values(i)
        if rows[0] == testcase:
             
             _headers=wb.row_values(i-1)
             _headers=[_header for _header in _headers if _header.strip()]
             break
             
    
    return ",".join(_headers[2:])



def read_data(testcases,sheetname):
    data=[]
    we=open_workbook("testdata.xls")
    wc=we.sheet_by_name(sheetname)
    used_rows=wc.nrows
    for i in range(0,used_rows):
        row=wc.row_values(i)
        
        if row[0]==testcases:
            temp_data=[i for i in row if i.strip()]
        
            if temp_data[1].upper()== 'YES':
                data.append(tuple(temp_data[2:]))
    return data

# print(read_data("test_login_positive","smoke"))
# print(read_headers("test_login_positive","smoke"))
print(read_locator('loginpage'))