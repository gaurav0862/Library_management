from tkinter import *
from tkinter.messagebox import *
from pymysql import *

class addcat:

    def __init__(self):
        self.top = Toplevel()
        self.top.title("ADD ADMIN")

        self.top.geometry('500x500')
        self.top.label_3 = Label(self.top, text="Sections", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,
                                                                                                              pady=20)
        self.label_1 = Label(self.top, text=" Name :: ").pack(side=TOP, pady=10)
        self.en = Entry(self.top)
        self.en.pack(side=TOP, pady=10)
        self.lable_2 = Label(self.top, text="Section Description").pack(side=TOP, pady=10)
        self.enp = Text(self.top, width=50, height=10)
        self.enp.pack(side=TOP)
        self.Button1 = Button(self.top, text='ADD', command=self.unewcat)
        self.Button1.pack(side=TOP, pady=10)


    def unewcat(self):

        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        if self.en=="" and self.enp=="":
            showinfo("ADD CATEGORY",'Please input correct details')
        else:
            q = 'insert into section values ("{}","{}")'.format(self.en.get(), self.enp.get(1.0, END))
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchall()
            showinfo("Section","Section Added Successfully")
            self.top.destroy()

