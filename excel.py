from openpyxl import Workbook
import os
from getdata import *

def make_excel(file_list):
    wb = Workbook()
    ws1 = wb.active
    failed = []
    for i, image in enumerate(file_list):
        exif = get_exif(image)
        coordi = get_coordinates(exif)
        if(coordi != False):
            ws1["A1"] = "Order"
            ws1["B1"] = "FileName"
            ws1["C1"] = "Latitude"
            ws1["D1"] = "Longitude"
            bh = ws1.column_dimensions["B"]
            bh.width = 30
            ch = ws1.column_dimensions["C"]
            ch.width = 20
            dh = ws1.column_dimensions["D"]
            dh.width = 20
            
            ws1["A"+str(2+i-len(failed))] = i+1-len(failed)
            ws1["B"+str(2+i-len(failed))] = os.path.basename(image)
            ws1["C"+str(2+i-len(failed))] = coordi[0]
            ws1["D"+str(2+i-len(failed))] = coordi[1]
        else:
            failed.append(image)
    wb.save("os.getcwd()" + "\\where_were_we.xlsx")
    return failed