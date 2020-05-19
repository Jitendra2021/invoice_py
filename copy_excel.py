import shutil
from win32com.client import Dispatch

def create_new_excel(name, bill_no):
    filename = name + "_" + str(bill_no)
    src_path = "D:\\Jitu\\srl_invoice\\resource\\test.xlsx"
    dest_path = "D:\\Jitu\\srl_invoice\\resource\\invoices\\"

    shutil.copy(src_path, dest_path + filename + ".xlsx" )


def copy_excel(name, bill_no):

    filename = name + "_" + str(bill_no)
    src_path = "D:\\Jitu\\srl_invoice\\resource\\test.xlsx"
    dest_path = "D:\\Jitu\\srl_invoice\\resource\\invoices\\"

    xl = Dispatch("Excel.Application")
    wb1 = xl.Workbooks.Open(Filename=src_path)

    wb2 = xl.Workbooks.Add()
    wb2.SaveAs(Filename = dest_path + filename + ".xlsx")

    ws1 = wb1.Worksheets(1)
    ws1.Copy(Before=wb2.Worksheets(1))

    wb2.Close(SaveChanges=True)
    xl.Quit()

