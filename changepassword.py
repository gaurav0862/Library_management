from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class change:

    def __init__(self,memid):
        self.memberid = memid
        self.top = Toplevel()
        self.top.title("ADD ADMIN")
        self.top.geometry('500x500')
        self.top.label_3 = Label(self.top, text="Change Password", font=("Constantia", "20", "italic", 'bold')).pack(
            side=TOP,
            pady=20)
        self.label_1 = Label(self.top, text="Email ID :: ").pack(side=TOP, pady=10)
        self.en = Entry(self.top)
        self.en.pack(side=TOP, pady=10)
        self.lable_2 = Label(self.top, text="Enter new password").pack(side=TOP, pady=10)
        self.enp = Entry(self.top)
        self.enp.pack(side=TOP,pady=10)
        self.Button1 = Button(self.top, text='ADD', command=self.unewcat)
        self.Button1.pack(side=TOP, pady=10)

    def unewcat(self):

        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()

        q = 'select emailID from addmembership where mId="{}"'.format(self.memberid)
        cr.execute(q)
        result = cr.fetchone()
        for i in result:
            self.new = i


        if self.en.get()== self.new:
            q = 'update addmembership set password = "{}" where mID="{}"'.format(self.enp.get(),self.memberid)
            cr.execute(q)
            conn.commit()
            self.top.destroy()
            showinfo('Change Password',"Password changed successfully")
        else:
            showerror('Change Password',"Invalid Email ID")





