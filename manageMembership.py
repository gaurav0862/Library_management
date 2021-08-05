from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview

from pymysql import *

class admin_view:

    def __init__(self):
        self.top = Toplevel()
        self.top.state("zoomed")
        self.top.title("Add Admin")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.var_3 = StringVar()
        self.top.geometry('500x500')
        self.labl = Label(self.top,text="Membership", font= ("Gabriola","25","italic",'bold')).pack(side= TOP,pady=5)
        self.label_1 = Label(self.top, text="Membership's Type ").pack(side=TOP, pady=10)
        self.type = Combobox(self.top,values=("Teacher","Student","Scholar's"),state='readonly')
        self.type.bind('<<ComboboxSelected>>', self.showdetails )
        self.type.pack(side=TOP,pady=10)
        # self.en = Entry(self.top, textvariable=self.var_1).pack(side=TOP, pady=10)
        self.lable_2 = Label(self.top, text="Books Allowed").pack(side=TOP, pady=10)
        self.enp = Entry(self.top, textvariable=self.var_2)
        self.enp.pack(side=TOP, pady=10)
        self.lable_2 = Label(self.top, text="Duration").pack(side=TOP, pady=10)
        self.entry = Entry(self.top,textvariable=self.var_3)
        self.entry.pack(side=TOP,pady=10)

        # self.upnew = Button(self.top, text='Update', command=self.upnew).pack(side=TOP, pady=10)


    def showdetails(self,event):
        self.eql = self.type.get()
        self.pml = self.var_2.get()
        self.pml_1 = self.var_2.get()

        self.enp.config(state='normal')
        self.entry.config(state='normal')
        self.enp.delete(0,END)
        self.entry.delete(0,END)


        if self.eql=="Teacher":
            conn = connect(host='127.0.0.1',user='root',password='',database='library_management')
            cr = conn.cursor()
            query = 'select * from membershiptype where typeName = "{}"'.format('Teacher')
            cr.execute(query)
            result = cr.fetchall()
            for i in result:
                self.enp.config(state='normal')
                self.entry.config(state='normal')
                self.enp.insert(0,i[1])
                self.entry.insert(0,i[2])
                self.entry.config(state='readonly')
                self.enp.config(state='readonly')
        elif self.eql == "Student":
            conn = connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            query = 'select * from membershiptype where typeName = "{}"'.format('Student')
            cr.execute(query)
            result = cr.fetchall()
            for i in result:
                self.enp.config(state='normal')
                self.entry.config(state='normal')
                self.enp.insert(0, i[1])
                self.entry.insert(0, i[2])
                self.entry.config(state='readonly')
                self.enp.config(state='readonly')
        elif self.eql == "Scholar's":
            conn = connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            query = 'select * from membershiptype where typeName = "{}"'.format('Scholar')
            cr.execute(query)
            result = cr.fetchall()
            for i in result:
                self.enp.config(state='normal')
                self.entry.config(state='normal')
                self.enp.insert(0, i[1])
                self.entry.insert(0, i[2])
                self.entry.config(state='readonly')
                self.enp.config(state='readonly')
