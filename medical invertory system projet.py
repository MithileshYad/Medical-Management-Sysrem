import tkinter
from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import os



class PharmacyManagementSystem:
    def __init__(self,medico):
        self.medico=medico
        self.medico.title("Pharmacy Management System")
        #self.medico.geometry("1550*800+0+0")

        #------------------AddMed Variable----------------------------------------------------------------------------
        self.refMedicine_var=StringVar()
        self.addMedicine_var=StringVar()



        lbtitle = Label(self.medico, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE
                        , bg='floral white', fg='darkgreen', font=("times new roman", 50, "bold"), padx=2, pady=4)

        lbtitle.pack(side=TOP, fill=X)

        img1=Image.open("E:\Pharma project\pharmalogo.jpeg")
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.medico,image=self.photoimg1,borderwidth=0)
        b1.place(x=20,y=18)

        #----------DATAFRAME----------------------------------------------------------#
        DataFrame=Frame(self.medico,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg='blue', font=("arial", 20, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight= LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department",
                                   fg='blue', font=("arial", 20, "bold"))
        DataFrameRight.place(x=910, y=5, width=550, height=350)

        #------------------BUTTONS FRAME---------------------------------------------------#

        ButtonFrame=Frame(self.medico, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=530, width=1530, height=65)

        #----------------MainnButton--------------------------------------------------------#
        btnAddData=Button(ButtonFrame, text="MEDICINE Add",width=15, font=("arial", 12, "bold"), bg="green", fg="black")
        btnAddData.grid(row=0, column=0)

        btnUpdateMedicine=Button(ButtonFrame, text="UPDATE",width=15, font=("arial", 12, "bold"), bg="green", fg="black")
        btnUpdateMedicine.grid(row=0, column=1)

        btnDeleteMedicine = Button(ButtonFrame, text="DELETE",width=15 ,font=("arial", 12, "bold"), bg="red", fg="black")
        btnDeleteMedicine.grid(row=0, column=2)

        btnResetMedicine= Button(ButtonFrame, text="RESET", width=15,font=("arial", 12, "bold"), bg="green", fg="black")
        btnResetMedicine.grid(row=0, column=3)

        btnExitMed= Button(ButtonFrame, text="EXIT", width=15,font=("arial", 12, "bold"), bg="green", fg="black")
        btnExitMed.grid(row=0, column=4)

        #---------------------SEARCH By-----------------------------------------------------------------------#
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="black")
        lblSearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",13, "bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame,bd=2,relief=RIDGE,width=12,font=("arial",13,))
        txtSearch.grid(row=0,column=7)

        searchbtn = Button(ButtonFrame, text="SEARCH", width=12,font=("arial", 12, "bold"), bg="green", fg="black")
        searchbtn.grid(row=0, column=8)

        showallbtn = Button(ButtonFrame, text="SHOW ALL", width=15,font=("arial", 12, "bold"), bg="green", fg="black")
        showallbtn.grid(row=0, column=9)



        #-------------------------------------label and entry-----------------------------------------------------
        lblrefno = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblrefno.grid(row=0, column=0, sticky=W)

        lblcomname = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Company Name:", padx=2,pady=5)
        lblcomname.grid(row=1, column=0, sticky=W)

        lblmedtype = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Type Of Medicine:", padx=2,pady=5 )
        lblmedtype.grid(row=2, column=0, sticky=W)

        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=5)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        lbllotno = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot Number:", padx=2, pady=5)
        lbllotno.grid(row=4, column=0, sticky=W)

        lblissuedate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=5)
        lblissuedate.grid(row=5, column=0, sticky=W)

        lblexpdate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=5)
        lblexpdate.grid(row=6, column=0, sticky=W)

        lbluses = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:", padx=2, pady=5)
        lbluses.grid(row=7, column=0, sticky=W)

        lblsideeff = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effects:", padx=2, pady=5)
        lblsideeff.grid(row=8, column=0, sticky=W)

        lblwarning= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prec&War:", padx=2, pady=5)
        lblwarning.grid(row=0, column=3, sticky=W)

        lbldosage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dosage:", padx=2, pady=5)
        lbldosage.grid(row=1, column=3, sticky=W)

        lbltabprice= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablet Price:", padx=2, pady=5)
        lbltabprice.grid(row=2, column=3, sticky=W)

        lblQT= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Product QT:", padx=2, pady=5)
        lblQT.grid(row=3, column=3, sticky=W)

        lblcare= Label(DataFrameLeft, font=("arial", 18, "bold"),fg="maroon",bg="white", text="Healthcare Is Wealth", padx=75)
        lblcare.grid(row=4, column=3, sticky=W)





        #-------------------Add MedicineLeft-------------------------------------------------#
        ref_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 13, "bold"), state="readonly")
        ref_combo["values"] = ("Ref", "Medname", "Lot")
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)

        txtcomname= Entry(DataFrameLeft, bd=2, relief=RIDGE, width=29,bg="white", font=("arial", 12,))
        txtcomname.grid(row=1, column=1)

        medtype_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 13, "bold"), state="readonly")
        medtype_combo["values"] = ("Tablet", "Capsule", "Syrup","Drops","Inhales","injection","Topical Medicine")
        medtype_combo.grid(row=2, column=1)
        medtype_combo.current(0)

        MedicineName_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 13, "bold"), state="readonly")
        MedicineName_combo["values"] = ("Paracetamol", "Rentac", "Koflet", "zifi","VixInhaler", "abc", "Citrazine")
        MedicineName_combo.grid(row=3, column=1)
        MedicineName_combo.current(0)

        txtlotno = Entry(DataFrameLeft, bd=2, relief=RIDGE, width=29, bg="white", font=("arial", 12,))
        txtlotno.grid(row=4, column=1)

        txtissue = Entry(DataFrameLeft, bd=2, relief=RIDGE, width=29, bg="white", font=("arial", 12,))
        txtissue.grid(row=5, column=1)

        txtexpdate =Entry(DataFrameLeft, bd=2, relief=RIDGE, width=29, bg="white", font=("arial", 12,))
        txtexpdate.grid(row=6, column=1)

        txtuses= Entry(DataFrameLeft, bd=2, relief=RIDGE, width=29, bg="white", font=("arial", 12,))
        txtuses.grid(row=7, column=1)

        txtsideeff= Entry(DataFrameLeft, bd=2, relief=RIDGE, width=29, bg="white", font=("arial", 12,))
        txtsideeff.grid(row=8, column=1)

        txtwarning = Entry(DataFrameLeft, bd=2, relief=RIDGE, width=20, bg="white", font=("arial", 12,))
        txtwarning.grid(row=0, column=3)

        txtdosge = Entry(DataFrameLeft, bd=2, relief=RIDGE, width=20, bg="white", font=("arial", 12,))
        txtdosge.grid(row=1, column=3)

        txttabprice= Entry(DataFrameLeft, bd=2, relief=RIDGE, width=20, bg="white", font=("arial", 12,))
        txttabprice.grid(row=2, column=3)

        txtQT= Entry(DataFrameLeft, bd=2, relief=RIDGE, width=20, bg="white", font=("arial", 12,))
        txtQT.grid(row=3, column=3)


        #---------------------------Images---------------------------------------------------------------------
        img2 = Image.open("E:\Pharma project\pills.jpeg")
        img2 = img2.resize((200, 135), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.medico, image=self.photoimg2, borderwidth=0)
        b1.place(x=500, y=357)

        img3 = Image.open("E:\Pharma project\capsule.jpg")
        img3 = img3.resize((200, 135), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.medico, image=self.photoimg3, borderwidth=0)
        b1.place(x=700, y=357)


        #----------------------------------DataFrameRight----------------------------------------------------------

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department",
                                    fg='blue', font=("arial", 20, "bold"))
        DataFrameRight.place(x=910, y=5, width=550, height=350)

        img4 = Image.open("E:\Pharma project\medical.jfif")
        img4 = img4.resize((250, 115), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.medico, image=self.photoimg4, borderwidth=0)
        b1.place(x=965, y=185)

        img5 = Image.open("E:\Pharma project\medicine.jfif")
        img5 = img5.resize((230, 115), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.medico, image=self.photoimg5, borderwidth=0)
        b1.place(x=1240, y=185)

        lblref = Label(DataFrameRight, font=("arial", 12, "bold"), text="Reference No.:", padx=6, pady=5)
        lblref.place(x=0,y=115)
        txtref = Entry(DataFrameRight,textvariable=self.refMedicine_var, bd=2, relief=RIDGE, width=20, bg="white", font=("arial", 12,))
        txtref.place(x=150,y=120)

        lblmedname = Label(DataFrameRight, font=("arial", 12, "bold"), text="Medicine Name:", padx=6, pady=5)
        lblmedname.place(x=0, y=145)
        txtmedname = Entry(DataFrameRight,textvariable=self.addMedicine_var,bd=2, relief=RIDGE, width=20, bg="white", font=("arial", 12,))
        txtmedname.place(x=150, y=150)

        #-------------------------------side Frame------------------------------------------------------------

        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=180,width=335,height=120)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),
                                         xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref.")
        self.medicine_table.column("ref",width=100)
        self.medicine_table.heading("medname",text="Medicine Name")
        self.medicine_table.column("medname",width=100)

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        #-------------------Medicine Add Button---------------------------------------------------------------
        down_fame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_fame.place(x=360,y=130,width=135,height=160)

        btnAddmed = Button(down_fame, text="ADD", width=12, font=("arial", 12, "bold"),pady=3, bg="cyan",
                            fg="black")
        btnAddmed.grid(row=0, column=0)

        btnupdate = Button(down_fame, text="UPDATE", width=12, font=("arial", 12, "bold"), pady=4, bg="lime",
                           fg="black")
        btnupdate.grid(row=1, column=0)

        btndelete = Button(down_fame, text="DELETE", width=12, font=("arial", 12, "bold"), pady=4, bg="brown",
                           fg="black")
        btndelete.grid(row=2, column=0)

        btnclr = Button(down_fame, text="CLEAR", width=12, font=("arial", 12, "bold"), pady=4, bg="purple",
                           fg="black")
        btnclr.grid(row=3, column=0)


        #---------------------------Frame Details------------------------------------------------------------
        framedetails=Frame(self.medico, bd=15,relief=RIDGE,)
        framedetails.place(x=0,y=590,width=1530,height=210)

        #-------------------------Main table and scrollbar----------------------------------------------------
        table_frame = Frame(self.medico, bd=15, relief=RIDGE,)
        table_frame.place(x=15, y=605, width=1500, height=180)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table=ttk.Treeview(table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate"
                                                 ,"expdate","uses","sideeffect","warning","dosage","price","productqt"),
                                         xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        #scroll_x.pack(side=BOTTOM, fill=X)
        #scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("tabletname", width=100)
        self.pharmacy_table.column("lotno", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideeffect", width=100)
        self.pharmacy_table.column("warning", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqt", width=100)

        #self.fetch_dataMed()


        #------------------------Add Medicine Functionality Declaration-----------------------------------------------
        def AddMed(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="Suryansh@123",database="medical")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into medicine(Ref,MedicineName), values(%s,%s)",(
                                                                   self.refMedicine_var.get(),
                                                                   self.addMedicine_var.get()
                                                                                              ))

            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success","Medicine Added")

        def fetch_dataMed(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="Suryansh@123", database="medical")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from medical")
            rows=my_cursor.fetchall()
            if len(rows)!= 0:
                self.medicine_table.delete(*self.medicine_table.get_children())
                for i in rows:
                    self.medicine_table.insert("",END,values=i)
                conn.commit()
            conn.close()



















if __name__ == "__main__":
    medico=Tk()
    obj=PharmacyManagementSystem(medico)
    medico.mainloop()
