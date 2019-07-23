import xlrd
from tkinter import filedialog

def main(file=None):
    log = open('roomCheck.txt', 'w+')
    file.close()
    if file is None:
        book = xlrd.open_workbook(filedialog.askopenfilename(title = "Select File",filetypes = (("xlsx files","*.xlsx"),("xls files","*.xls"),("all files","*.*"))))
    else:
        book = xlrd.open_workbook(file)

    sheet = book.sheet_by_index(0)

    check = True

    roomCol = 0

    try:
        for row in range(sheet.nrows):
            firstTeam = sheet.cell(row, roomCol).value.replace('-ii','').replace('-i','')
            secondTeam = sheet.cell(row + 1, roomCol).value.replace('-ii','').replace('-i','')

            if firstTeam != secondTeam:
                continue

            for col in range(sheet.ncols):
                first_cell = sheet.cell(row, col).value
                second_cell = sheet.cell(row + 1, col).value

                if 'judge' in first_cell.lower() or 'judge' in second_cell.lower():
                    if 'field' in first_cell.lower() or 'field' in second_cell.lower():
                        None
                    else:
                        check = False
                        log = open('roomCheck', 'a+')
                        log.write('col:{col}\trow:{row}'.format(col=col, row=row))
                        log.close()
    
                    
    except:
        None

    if check:
        print('RoomCheck has been cleared')
    else:
        print('1 or more room failed please check roomCheck.txt for more details')

    return check

if __name__ == "__main__":
    main()