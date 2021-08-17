from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class member_view:

    def __init__(self):
            self.top = Toplevel()
            self.top.title("View Membership")
            self.style = ttk.Style()
            self.style.theme_use('clam')
            self.top.label_3 = Label(self.top, text="Members", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,pady=5)
            self.top.waraper = LabelFrame(self.top)
            self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=10)
            self.trv = Treeview(self.top.waraper, columns=(1, 2, 3, 4,5,6,7,8,9), show="headings", height="5")
            self.trv.pack(padx=10, pady=50)
            self.trv.column("# 1", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 2", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 3", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 4", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 5", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 6", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 7", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 8", anchor=CENTER, stretch=NO, width=100)
            self.trv.column("# 9", anchor=CENTER, stretch=NO, width=100)
            self.trv.heading(1, text="Member ID")
            self.trv.heading(2, text="Name")
            self.trv.heading(3, text="F.Name")
            self.trv.heading(4, text="Mob.No")
            self.trv.heading(5, text="Email ID")
            self.trv.heading(6, text="Membership Type")
            self.trv.heading(7, text="Status")
            self.trv.heading(8, text="Password")
            self.trv.heading(9, text="Books Alloted")
            self.trv.bind("<Double-1>", self.show_adddetails)
            conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            q = 'select * from addmembership'
            cr.execute(q)
            self.result = cr.fetchall()

            for i in self.trv.get_children():
                self.trv.delete(i)

            for i in self.result:
                self.trv.insert("", END, value=i)

    def show_adddetails(self, event):
            self.temp_data = self.trv.item(self.trv.focus())['values']
            self.top = Toplevel()
            self.top.geometry('500x500')
            Label(self.top, text="Member ID: ").grid(row=0,column=1)
            self.em = Entry(self.top)
            self.em.insert(0, self.temp_data[0])
            self.em.config(state="readonly")
            self.em.grid(row=0,column=2)
            Label(self.top, text="Name: ").grid(row=1,column=1)
            self.pm = Entry(self.top)
            self.pm.insert(0, self.temp_data[1])
            self.pm.grid(row=1,column=2)
            Label(self.top, text="Father's Name: ").grid(row=2,column=1)
            self.ll = Entry(self.top)
            self.ll.insert(0, self.temp_data[2])
            self.ll.grid(row=2,column=2)
            Label(self.top, text="Mobile No.: ").grid(row=3, column=1)
            self.ll = Entry(self.top)
            self.ll.insert(0, self.temp_data[3])
            self.ll.grid(row=3, column=2)
            Label(self.top, text="Email ID: ").grid(row=4, column=1)
            self.ll = Entry(self.top)
            self.ll.insert(0, self.temp_data[4])
            self.ll.grid(row=4, column=2)
            Label(self.top, text="Membership Type ").grid(row=5, column=1)
            self.enp_1 = ("Teacher","Student","Scholar")
            self.current = self.enp_1.index(str(self.temp_data[5]))
            self.enl = Combobox(self.top, values=self.enp_1, state="readonly")
            self.enl.current(self.current)
            self.enl.insert(0, self.temp_data[5])
            self.enl.config(state='readonly')
            self.enl.grid(row=5, column=2)


            Label(self.top, text="Status ").grid(row=6, column=1)
            self.enp_2 = ("Active","Not Active")
            self.current = self.enp_2.index(str(self.temp_data[6]))
            self.enl = Combobox(self.top, values=self.enp_2, state="readonly")
            self.enl.current(self.current)
            self.enl.grid(row=6, column=2)
            self.enl.insert(0, self.temp_data[6])
            self.enl.config(state='readonly')

            Label(self.top, text="Password: ").grid(row=7, column=1)
            self.ll = Entry(self.top)
            self.ll.insert(0, self.temp_data[7])
            self.ll.config(state='readonly')
            self.ll.grid(row=7, column=2)





            # self.upbtn = Button(self.top, text="update", command=self.newupdate)
            # self.upbtn.pack()
            # self.delbtn = Button(self.top, text="Delete", command=self.delupdate)
            # self.delbtn.pack()

        #     # --------------UPDATE EXISTING ADMIN DATA--------------
        #
        # def newupdate(self):
        #     self.pqw = self.pm.get()
        #     self.eml = self.em.get()
        #     self.rol = self.enl.get()
        #     conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        #     cr = conn.cursor()
        #     q = 'update adminmember set password="{}",adminType="{}" where email="{}"'.format(self.pqw, self.rol,
        #                                                                                       self.eml, )
        #
        #     cr.execute(q)
        #     print(q)
        #     conn.commit()
        #     self.result = cr.fetchall()
        #     self.top.destroy()
        #
        #     # ------------DELETE SELECTED ADMIN DATA----------------
        #
        # def delupdate(self):
        #     self.eml = self.em.get()
        #     conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        #     cr = conn.cursor()
        #     q = 'delete from adminmember where email="{}"'.format(self.eml)
        #
        #     cr.execute(q)
        #     print(q)
        #     conn.commit()
        #     self.result = cr.fetchall()
        #
        #     for i in self.trv.get_children():
        #         self.trv.delete(i)
        #
        #     for i in self.result:
        #         self.trv.insert("", END, value=i)
        #     self.top.destroy()