from tkinter import *
from PIL import Image,ImageTk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

import viewBooks
import viewSubsection
import addAdmin
import addBooks
import addSection
import addSubSection
import viewAdmin
import viewSections
import manageMembership
import addMembership


class demo:

    def __init__(self):
        self.root = Tk()
        self.root.title("Home Page")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry('1366x680+0+0')
        self.root.resizable(0, 0)
        self.homeimg = Image.open("image resources/header-bg.png")
        self.resized_image = self.homeimg.resize((1366,748),Image.ANTIALIAS)
        self.newimg = ImageTk.PhotoImage(self.resized_image)
        self.canvas1 = Canvas(self.root)
        self.canvas1.pack(fill="both", expand=True)

        self.canvas1.create_image(0, 0, image=self.newimg, anchor='nw')

        self.canvas1.create_text(700, 50, text="Reading Room at the British Museum", font=("Gabriola", "50", "italic", 'bold'),fill="white")
        self.canvas1.create_text(690, 125, text="Search Member ", font=("Gabriola", "20", 'bold'),fill="white")


        self.menu_1 = Menu(self.root)
        self.root.config(menu=self.menu_1)
        self.admin = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Admin", menu=self.admin)
        self.admin.add_command(label="Add User", command=lambda: addAdmin.admin_view())
        self.admin.add_command(label="View Admin", command=lambda: viewAdmin.viewadd())
        self.admin.add_command(label="Logout", command=self.logout)
        self.catmenu = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Section", menu=self.catmenu)
        self.catmenu.add_command(label="Add Section", command=lambda: addSection.addcat())
        self.catmenu.add_command(label="View Sections", command=lambda: viewSections.viewsec())
        self.promenu = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Sub Section", menu=self.promenu)
        self.promenu.add_command(label="Add Subsection", command=lambda: addSubSection.addpro())
        self.promenu.add_command(label="View Subsection", command=lambda: viewSubsection.viewsubsec())
        self.storeview = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Books", menu=self.storeview)
        self.storeview.add_command(label="Add Book", command=lambda: addBooks.addpro())
        self.storeview.add_command(label="View Book", command=lambda: viewBooks.viewbook())
        self.membership = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Manage Memberships", menu=self.membership)
        self.membership.add_command(label="Memberships type", command=lambda: manageMembership.admin_view())
        self.membership.add_command(label="ADD Memberships", command=lambda: addMembership.member_add())
        self.membership = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Issued Books", menu=self.membership)
        self.membership.add_command(label="View Issued Books", command=lambda: viewbooksisued.issue())
        self.canvas1.create_text(450,200,text="Serch By :",font=("arial", "15", "bold", 'bold'),fill="white")
        self.type=Combobox(self.canvas1,values=("ID","Name","Mobile"),state="readonly")
        self.type.current(0)
        self.type.place(x=518,y=189)
        self.entry = Entry(self.canvas1,width=28)
        self.entry.place(x=700,y=189)
        self.btn = Button(self.canvas1,text="Search",font=("arial", "10", "bold", 'bold'),command=self.search,width=15)
        self.btn.place(x=540,y=235)
        self.btn = Button(self.canvas1,text="Fetch All",font=("arial", "10", "bold", 'bold'),command=self.fetchall,width=15)
        self.btn.place(x=680,y=235)

        self.root.mainloop()

    def fetchall(self):

        conn = connect(host="127.0.0.1", user="root", password="", database="library_management")
        cr = conn.cursor()
        q = 'select * from addmembership'
        cr.execute(q)
        result = cr.fetchall()
        self.top = Toplevel()
        Label(self.top, text="RESULT", font=("Gabriola", "50", "italic", 'bold')).pack(side=TOP)
        self.type.config(state="normal")

        self.trv1 = Treeview(self.top, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="5")
        self.trv1.pack(padx=10, pady=10)
        self.trv1.column("# 1", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 2", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 3", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 4", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 5", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 6", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 7", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 8", anchor=CENTER, stretch=NO, width=100)

        self.trv1.heading(1, text="Member ID")
        self.trv1.heading(2, text="Name")
        self.trv1.heading(3, text="Father's Name")
        self.trv1.heading(4, text="Mobile")
        self.trv1.heading(5, text="Email")
        self.trv1.heading(6, text="Type")
        self.trv1.heading(7, text="Status")
        self.trv1.heading(8, text="Password")

        for i in self.trv1.get_children():
            self.trv1.delete(i)

        for i in result:
            self.trv1.insert("", END, value=i)

    def search(self):
        st = self.type.get()
        field = self.entry.get()

        if field == "":

            showwarning('Search', "Entry field should not be empty")

        elif st == "ID":

            conn = connect(host="127.0.0.1", user="root", password="", database="library_management")
            cr = conn.cursor()
            q = 'select * from addmembership where mId= "{}"'.format(field)
            cr.execute(q)
            result = cr.fetchall()

            if result == ():
                showerror('Search', "No Data Found")

            else:

                self.top = Toplevel()
                Label(self.top, text="RESULT", font=("Gabriola", "50", "italic", 'bold')).pack(side=TOP)
                self.type.config(state="normal")

                self.trv1 = Treeview(self.top, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="5")
                self.trv1.pack(padx=10, pady=10)
                self.trv1.column("# 1", anchor=CENTER, stretch=NO, width=100)
                self.trv1.column("# 2", anchor=CENTER, stretch=NO, width=100)
                self.trv1.column("# 3", anchor=CENTER, stretch=NO, width=100)
                self.trv1.column("# 4", anchor=CENTER, stretch=NO, width=100)
                self.trv1.column("# 5", anchor=CENTER, stretch=NO, width=100)
                self.trv1.column("# 6", anchor=CENTER, stretch=NO, width=100)
                self.trv1.column("# 7", anchor=CENTER, stretch=NO, width=100)
                self.trv1.column("# 8", anchor=CENTER, stretch=NO, width=100)

                self.trv1.heading(1, text="Member ID")
                self.trv1.heading(2, text="Name")
                self.trv1.heading(3, text="Father's Name")
                self.trv1.heading(4, text="Mobile")
                self.trv1.heading(5, text="Email")
                self.trv1.heading(6, text="Type")
                self.trv1.heading(7, text="Status")
                self.trv1.heading(8, text="Password")

                for i in self.trv1.get_children():
                    self.trv1.delete(i)

                for i in result:
                    self.trv1.insert("", END, value=i)


        elif st == "Name":
            conn = connect(host="127.0.0.1", user="root", password="", database="library_management")
            cr = conn.cursor()
            q = 'select * from addmembership where memberName = "{}"'.format(field)
            cr.execute(q)
            result = cr.fetchall()

            self.top = Toplevel()
            Label(self.top, text="RESULT", font=("Gabriola", "50", "italic", 'bold')).pack(side=TOP)
            self.type.config(state="normal")

            self.trv1 = Treeview(self.top, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="5")
            self.trv1.pack(padx=10, pady=10)
            self.trv1.column("# 1", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 2", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 3", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 4", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 5", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 6", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 7", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 8", anchor=CENTER, stretch=NO, width=100)

            self.trv1.heading(1, text="Member ID")
            self.trv1.heading(2, text="Name")
            self.trv1.heading(3, text="Father's Name")
            self.trv1.heading(4, text="Mobile")
            self.trv1.heading(5, text="Email")
            self.trv1.heading(6, text="Type")
            self.trv1.heading(7, text="Status")
            self.trv1.heading(8, text="Password")

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in result:
                self.trv1.insert("", END, value=i)


        elif st == "Mobile":

            conn = connect(host="127.0.0.1", user="root", password="", database="library_management")
            cr = conn.cursor()
            q = 'select * from addmembership where mobileNo = "{}"'.format(field)
            cr.execute(q)
            result = cr.fetchall()

            self.top = Toplevel()
            Label(self.top, text="RESULT", font=("Gabriola", "50", "italic", 'bold')).pack(side=TOP)
            self.type.config(state="normal")

            self.trv1 = Treeview(self.top, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="5")
            self.trv1.pack(padx=10, pady=10)
            self.trv1.column("# 1", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 2", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 3", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 4", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 5", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 6", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 7", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 8", anchor=CENTER, stretch=NO, width=100)

            self.trv1.heading(1, text="Member ID")
            self.trv1.heading(2, text="Name")
            self.trv1.heading(3, text="Father's Name")
            self.trv1.heading(4, text="Mobile")
            self.trv1.heading(5, text="Email")
            self.trv1.heading(6, text="Type")
            self.trv1.heading(7, text="Status")
            self.trv1.heading(8, text="Password")

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in result:
                self.trv1.insert("", END, value=i)


    def logout(self):
            self.root.destroy()




obj = demo()