from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *


class addpro:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("ADD Subsection")
        self.var_1 = StringVar()

        self.top.geometry('500x500')
        # self.top.state("zoomed")
        self.top.label_5 = Label(self.top, text="ADD Subsection", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,
                                                                                                                 pady=20)
        self.label_1 = Label(self.top, text="Sub Section Name :: ",font=("Gabriola", "15", "bold")).place(x=120, y=100)
        self.en1 = Entry(self.top, textvariable=self.var_1).place(x=280, y=110)
        self.label_4 = Label(self.top, text="Section Name ::" ,font=("Gabriola", "15", "bold")).place(x=120, y=150)
        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        q = 'select sectionName from section'
        cr.execute(q)
        conn.commit()
        self.result = cr.fetchall()
        x = []
        for i in self.result:
            x.append(i[0])
        self.enl = Combobox(self.top, values=x, state="readonly")
        self.enl.place(x=260, y=160)

        self.Button1 = Button(self.top, text='ADD', command=self.newpro)
        self.Button1.place(x=250, y=200)


    def newpro(self):
        self.pnam = self.var_1.get()
        self.cat = self.enl.get()
        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        if self.pnam==""  or  self.cat=="":
            showinfo("ADD Subsection","Provide valid inputs")
        else:
                q = 'insert into subsection values ("{}","{}")'.format( self.pnam,self.cat)
                cr.execute(q)
                conn.commit()
                self.result = cr.fetchall()
                showinfo('Add Subsection','Subsection Added successfully')
                self.top.destroy()

