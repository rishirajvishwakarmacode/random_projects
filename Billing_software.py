from tkinter import *
from datetime import date, datetime

class Bill_app :
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Variety book house")
        title=Label(self.root, text ='Billing Software', font=('time new roman', 30, 'bold'), pady=2).pack(fill = X)

        # ============================Variables====================================
        self.customer_name = StringVar()
        self.customer_phone_number = IntVar()
        self.bill_no = IntVar()
        self.product_name = StringVar()
        self.product_price = IntVar()
        self.total_bill = StringVar()
        self.tax = StringVar()
        self.payable_bill = StringVar()

        self.price_list = []

        self.product_list  = []

        self.index = 1



        # customer details
        F1 = LabelFrame(self.root, text='Customer details', font=('times new roman', 15, "bold"))
        F1.place(x=0,y=60,relwidth=1)

        customer_name_lbl = Label(F1, text='customer name', font= ('times new roman', 10)).grid(row=0, column=0, padx=20)
        customer_name_field = Entry(F1,textvariable=self.customer_name, width=15, font='arial 15').grid(row=0, column=1, padx=2, pady=5)

        customer_phone_lbl = Label(F1, text='Phone number', font= ('times new roman', 10)).grid(row=0, column=2, padx=20)
        customer_phone_field = Entry(F1, textvariable=self.customer_phone_number, width=15, font='arial 15').grid(row=0, column=3, padx=2, pady=5)

        customer_bill_lbl = Label(F1, text='Bill No', font= ('times new roman', 10)).grid(row=0, column=4, padx=20)
        customer_bill_field = Entry(F1, textvariable=self.bill_no, width=15, font='arial 15').grid(row=0, column=5, padx=2, pady=5)

        bill_btn = Button(F1, text='Search', width=10).grid(row=0, column=6)

        # books frame        
        F2 = LabelFrame(self.root, text='Books', font=('times new roman', 15, "bold"))
        F2.place(x=5,y=170,width=325, height=380)

        book_lbl= Label(F2, text="enter product name").grid(row=0, column=0)
        book_name_field = Entry(F2,textvariable=self.product_name, width=20).grid(row=1, column=1)

        book_price_lbl= Label(F2, text="enter product Price").grid(row=2, column=0)
        book_price_field=Entry(F2, textvariable=self.product_price, width=20).grid(row=3, column=1)

        add_to_bill_btn = Button(F2,command=self.addtobill, text='Add To Bill').grid(row=4, column=1)


        # stationary frame       
        F4 = LabelFrame(self.root, text='Stationary', font=('times new roman', 15, "bold"))
        F4.place(x=500,y=170,width=325, height=380)       


        # bill area 
        F3 = LabelFrame(self.root)
        F3.place(x=1000,y=170,width=325, height=380)
        bill_title = Label(F3, text='Billarea', font=('times new roman', 15)).pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txtarea = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.insert('end-1c', "           Variety Book Store              \n                Bhopal              \n\n\n===========================================\n Costumer name : {}\n Product name                     Price\n===========================================".format(self.customer_name.get()))
        self.txtarea.pack(fill=BOTH)

        # calculation area 
        
        f6=LabelFrame(self.root, text='Total area', font=('times new roman', 15))
        f6.place(x=0, y=550)
        total_bill_label= Label(f6, text='Total Bill amount', font=(10)).grid(row=0, column=0)
        total_bill_field = Entry(f6, textvariable=self.total_bill, width=15).grid(row=0,column=1, padx=5)

        tax_label= Label(f6, text='Tax on bill', font=(10)).grid(row=1, column=0)
        tax_field = Entry(f6,textvariable=self.tax, width=15).grid(row=1,column=1, padx=0)

        payable_label= Label(f6, text='amount payable', font=(10)).grid(row=2, column=0)
        payable_field = Entry(f6,textvariable=self.payable_bill, width=15).grid(row=2,column=1, padx=0)


        Total_btn = Button(f6, command=self.total, text='Total').grid(row=2,column=2, pady=11, padx=5)

        generate_btn = Button(f6, text='generate').grid(row=2,column=3, pady=11, padx=5)

        clear_btn = Button(f6, text='Clear').grid(row=2,column=4, pady=11, padx=5)

        root.update()
        
    def addtobill(self):
        
        self.price_list.append(self.product_price.get())
        self.product_list.append(self.product_name.get())
        self.txtarea.insert('end-1c', self.product_name.get() + "                      " + str(self.product_price.get()) + '\n')
        print (self.price_list)

    def total(self):
        print('triggered')
        taxable_bill = 0
        for item in self.price_list:
            taxable_bill += item
        tax = 0.18*taxable_bill
        payable_bill_final = taxable_bill + tax

        # self.total_bill = taxable_bill
        # self.tax = tax
        # self.payable_bill = payable_bill_final
        self.total_bill.set(str(taxable_bill))
        self.tax.set(str(tax))
        self.payable_bill.set(str(payable_bill_final))

        self.txtarea.insert('end-1c', "=========================================\n Total amount payable: {}\n Tax: {}\n Billed amount: {}".format(payable_bill_final, tax, taxable_bill))




    


        


    






root = Tk()
obj = Bill_app(root)
root.mainloop()