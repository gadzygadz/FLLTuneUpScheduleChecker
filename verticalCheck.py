import xlrd
from tkinter import filedialog

def main(file = None):

    log = open('verticalCheck.txt', 'w+')
    log.close()

    if file is None:
        book = xlrd.open_workbook(filedialog.askopenfilename(title = "Select File",filetypes = (("xlsx files","*.xlsx"),("xls files","*.xls"),("all files","*.*"))))
    else:
        book = xlrd.open_workbook(file)

    sheet = book.sheet_by_index(0)

    nrows = sheet.nrows - 1
    ncols = sheet.ncols - 1

    check = True

    for col in range(ncols):
        hits = []
        for row in range(nrows):
            if sheet.cell(row, col).value not in hits:
                hits.append(sheet.cell(row, col).value)
            else:
                check = False
                log = open('verticalCheck.txt', 'a+')
                log.write('col:{col}\trow:{row}\trepeat_value:{value}'.format(col=col, row=row, value=sheet.cell(col,row).value))
                log.close()
    if check:
        print('Vertical Checks passed')
    else:
        print('1 or more Vertical Checks failed see more info @ verticalCheck.txt')
    
    return check
