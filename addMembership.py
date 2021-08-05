from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
import random

import mails125



from pymysql import *

class member_add:

    def __init__(self):
        self.top = Toplevel()

        self.top.geometry('600x600')
        self.top.resizable(0,0)
        self.top.title("Add Admin")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.panewin = PanedWindow(self.top)
        Label(self.panewin, text="Add Membership", font=("Gabriola", "25", "italic", 'bold'),pady=20).pack(side=TOP)
        self.panewin.pack()

        self.panewin1= PanedWindow(self.top)
        self.panewin1.pack()
        Label(self.panewin1, text="Name :").grid(row=0, column=0,pady=5)
        self.name = Entry(self.panewin1)
        self.name.grid(row=0,column=1,pady=5,padx=7)
        Label(self.panewin1, text="Father's Name :").grid(row=1, column=0,padx=7)
        self.fatherName = Entry(self.panewin1)
        self.fatherName.grid(row=1,column=1,pady=5,padx=7)
        Label(self.panewin1, text="Mobile :").grid(row=2, column=0,padx=7)
        self.mobile = Entry(self.panewin1)
        self.mobile.grid(row=2,column=1,pady=5,padx=7)
        Label(self.panewin1, text="Email :").grid(row=3, column=0,padx=7)
        self.Email = Entry(self.panewin1)
        self.Email.grid(row=3,column=1,pady=5,padx=7)
        Label(self.panewin1, text="Membership's Type : ").grid(row=4,column=0,padx=7)
        conn = connect(host="127.0.0.1",user="root",password="",database="library_management")
        cr = conn.cursor()
        q = 'select * from membershiptype'
        cr.execute(q)
        result=cr.fetchall()
        x = []
        for i in result:
            x.append(i[0])
        self.type = Combobox(self.panewin1, values=x, state='readonly')
        self.type.grid(row=4, column=1)
        Label(self.panewin1, text="status :").grid(row=5, column=0, padx=7)
        self.status = Combobox(self.panewin1, values=('Active','Not Active'), state='readonly')
        self.status.grid(row=5, column=1, pady=5, padx=7)

        btton = Button(self.top,text="ADD",command= self.addmember ,width=15)
        btton.pack(pady=15)



    def addmember(self):

        Email=self.Email.get()
        Name = self.name.get()
        MAX_LEN = 12
        randompass = "qwertyuiopasdfghjklzxcvbnm,1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
        password ="".join(random.sample(randompass,MAX_LEN))

        if self.name.get()=="" and self.fatherName.get()=="" and self.mobile.get()=="" and self.Email.get()=="" and self.status.get()=="" and self.type.get()=="":
            showinfo("ADD ADMIN","Please provide input all inputs")

        else:
            conn = connect(host='127.0.0.1',user='root',password='',database='library_management')
            cr = conn.cursor()
            q = 'select * from addmembership where emailId="{}" '.format(self.Email.get())
            cr.execute(q)
            result = cr.fetchone()
            print(result)
            if result==None:
                conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
                cr = conn.cursor()
                q = 'insert into addmembership values (null,"{}","{}","{}","{}","{}","{}","{}")'.format(self.name.get(), self.fatherName.get(),self.mobile.get(),self.Email.get(),self.type.get(),self.status.get(),password)
                cr.execute(q)
                conn.commit()
                self.top.destroy()
                mails125.mailing(Email, "New login to Reading Room at the British Museum",
                                 f"Hi, {Name} password for your login is  {password}")
            else:
                showerror('Add Admin','Email Already Taken')
                self.top.destroy()


