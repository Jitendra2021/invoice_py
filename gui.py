from tkinter import *
parent = Tk()

def retrieve_input():
    company_name = e1.get()
    address = e2.get()
    gstin_no = e3.get()
    bill_date = e4.get()
    bill_no = e5.get()
    lr_no = e6.get()
    source = e7.get()
    destination = e8.get()
    rate = e9.get()
    amount = e10.get()
    cgst = e11.get()
    sgst = e12.get()
    other_charge = e13.get()

    print(address, lr_no)


parent.title('S.R Logistics - Generate Invoice')


label1 = Label(parent, text="S.R Logistics - Generate Invoice", font=("Helvetica", 16), justify=CENTER, fg="red", anchor=CENTER)
label1.grid()

company_name = Label(parent, text="company_name").grid()
e1 = Entry(parent)
e1.grid(row=1, column=1)

address = Label(parent, text="address").grid(row=2, column=0)
e2 = Entry(parent)
e2.grid(row=2, column=1)

gstin_no = Label(parent, text="gstin_no").grid(row=3, column=0)
e3 = Entry(parent)
e3.grid(row=3, column=1)

bill_date = Label(parent, text="bill_date").grid(row=1, column=2)
e4 = Entry(parent)
e4.grid(row=1, column=3)

bill_no = Label(parent, text="bill_no").grid(row=2, column=2)
e5 = Entry(parent)
e5.grid(row=2, column=3)

lr_no = Label(parent, text="lr_no").grid(row=4, column=0)
e6 = Entry(parent)
e6.grid(row=4, column=1)

source = Label(parent, text="source").grid(row=5, column=0)
e7 = Entry(parent)
e7.grid(row=5, column=1)

destination = Label(parent, text="destination").grid(row=5, column=2)
e8 = Entry(parent)
e8.grid(row=5, column=3)

rate = Label(parent, text="rate").grid(row=6, column=0 )
e9 = Entry(parent)
e9.grid(row=6, column=1)

amount = Label(parent, text="amount").grid(row=7, column=0)
e10 = Entry(parent)
e10.grid(row=7, column=1)

cgst = Label(parent, text="cgst").grid(row=8, column=0)
e11 = Entry(parent)
e11.grid(row=8, column=1)

sgst = Label(parent, text="sgst").grid(row=8, column=2)
e12 = Entry(parent)
e12.grid(row=8, column=3)

other_charge = Label(parent, text="other_charge").grid(row=9, column=0)
e13 = Entry(parent)
e13.grid(row=9, column=1)

submit = Button(parent, text="Generate Invoice", command=retrieve_input).grid(row=12, column=0)

parent.mainloop()
