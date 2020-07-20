from win32com import client

def excel_to_pdf():
    xlApp = client.Dispatch("Excel.Application")
    books = xlApp.Workbooks.Open('D:\\Jitu\\srl_invoice\\resource\\invoices\\kkkkk_34534.xlsx')
    ws = books.Worksheets[0]

    ws.ExportAsFixedFormat(0, "D:\\Jitu\\srl_invoice\\resource\\invoices\\trial.pdf")

excel_to_pdf()