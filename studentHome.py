from tkinter import *
from PIL import Image,ImageTk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *
import datetime
from datetime import datetime, timedelta

import changepassword
import viewissuedbooks


class student:

    def __init__(self,lgv,lgv2,lgv3):
        self.memberId = lgv
        self.membertype = lgv2
        self.booksalloted = lgv3
        self.root = Tk()
        self.root.title("Home Page")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry('1366x680+0+0')
        self.root.resizable(0, 0)
        self.homeimg = Image.open("image resources/janko-ferlic-sfL_QOnmy00-unsplash.jpg")
        self.resized_image = self.homeimg.resize((1366,748),Image.ANTIALIAS)
        self.newimg = ImageTk.PhotoImage(self.resized_image)
        self.canvas1 = Canvas(self.root)
        self.canvas1.pack(fill="both", expand=True)

        self.canvas1.create_image(0, 0, image=self.newimg, anchor='nw')

        self.canvas1.create_text(700, 50, text="Reading Room at the British Museum",
                                 font=("Gabriola", "50", "italic", 'bold'), fill="white")
        self.canvas1.create_text(690, 125, text="Search Book ", font=("Gabriola", "20", 'bold'), fill="white")

        self.canvas1.create_text(580, 200, text="Search : ", font=("arial", "15", "bold", 'bold'), fill="white")
        self.entry = Entry(self.canvas1, width=28)
        self.entry.place(x=630, y=189)
        self.btn = Button(self.canvas1, text="Search", font=("arial", "10", "bold", 'bold'), command=self.search,
                          width=15)
        self.btn.place(x=540, y=235)
        self.btn = Button(self.canvas1, text="Fetch All", font=("arial", "10", "bold", 'bold'), command=self.fetchall,
                          width=15)
        self.btn.place(x=680, y=235)

        self.menu_1 = Menu(self.root)
        self.root.config(menu=self.menu_1)
        self.admin = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Profile", menu=self.admin)
        self.admin.add_command(label="Change Password", command=lambda: changepassword.change(self.memberId))
        self.admin.add_command(label="Logout", command=self.logout)
        self.Book = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Book", menu=self.Book)
        self.Book.add_command(label="View Issued Books", command=lambda: viewissuedbooks.issue(self.memberId))
        self.Book.add_command(label="Logout", command="self.logout")

        self.root.mainloop()

    def search(self):

        BBD = self.entry.get()

        conn = connect(host="127.0.0.1", user="root", password="", database="library_management")
        cr = conn.cursor()
        q = 'select * from books where bookId = "{}" or bookName ="{}" or author="{}" or editor="{}" or ISBN="{}" or SectionName="{}" or subSectionname="{}"'.format(
            BBD, BBD, BBD, BBD, BBD, BBD, BBD)
        cr.execute(q)
        result = cr.fetchall()
        print(result)

        if result == ():
            showerror('Search', "No Data Found")

        else:

            self.top = Toplevel()
            Label(self.top, text="RESULT", font=("Gabriola", "40", 'bold')).pack(side=TOP)
            self.top.waraper = LabelFrame(self.top, text="Books Details")
            self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)

            self.trv1 = Treeview(self.top.waraper, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings", height="5")
            self.trv1.pack(padx=10, pady=10)
            self.trv1.column("# 1", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 2", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 3", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 4", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 5", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 6", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 7", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 8", anchor=CENTER, stretch=NO, width=100)
            self.trv1.column("# 9", anchor=CENTER, stretch=NO, width=100)
            self.trv1.heading(1, text="Book ID")
            self.trv1.heading(2, text="Book Name")
            self.trv1.heading(3, text="Book Author")
            self.trv1.heading(4, text="Editor")
            self.trv1.heading(5, text="No. of topics")
            self.trv1.heading(6, text="Description")
            self.trv1.heading(7, text="ISBN")
            self.trv1.heading(8, text="Section")
            self.trv1.heading(9, text="Sub Section")

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in result:
                self.trv1.insert("", END, value=i)

    def fetchall(self):

        conn = connect(host="127.0.0.1", user="root", password="", database="library_management")
        cr = conn.cursor()
        q = 'select * from books'
        cr.execute(q)
        result = cr.fetchall()

        self.top = Toplevel()
        Label(self.top, text="RESULT", font=("Gabriola", "40", 'bold')).pack(side=TOP)
        self.top.waraper = LabelFrame(self.top, text="Books Details")
        self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=40)

        self.trv1 = Treeview(self.top.waraper, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings", height="5")
        self.trv1.pack(padx=10, pady=10)
        self.trv1.column("# 1", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 2", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 3", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 4", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 5", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 6", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 7", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 8", anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 9", anchor=CENTER, stretch=NO, width=100)
        self.trv1.heading(1, text="Book ID")
        self.trv1.heading(2, text="Book Name")
        self.trv1.heading(3, text="Book Author")
        self.trv1.heading(4, text="Editor")
        self.trv1.heading(5, text="No. of topics")
        self.trv1.heading(6, text="Description")
        self.trv1.heading(7, text="ISBN")
        self.trv1.heading(8, text="Section")
        self.trv1.heading(9, text="Sub Section")
        self.butn = Button(self.top,text = "Book",font=("arial", "10", 'bold'),command= self.book)
        self.butn.pack(pady=10)


        for i in self.trv1.get_children():
            self.trv1.delete(i)

        for i in result:
            self.trv1.insert("", END, value=i)

    def book(self):

        conn = connect(host="127.0.0.1",user="root",password='',database="library_management")
        cr= conn.cursor()
        self.temp_data = self.trv1.item(self.trv1.focus())['values']
        bookId = self.temp_data[0]

        time = datetime.date.today()


        if self.membertype=="Scholar":
            q = 'select booksAllowed,duration from membershiptype where typeName = "{}"'.format("scholar")
            cr.execute(q)
            result = cr.fetchall()
            print(result)

            x=[]
            for i in result:
                x.append(i[0])
                duration=i[1]
            if x[0]==self.booksalloted:
                showwarning("booking","Exceed limit ")
            else:
                new_date = datetime.date.today() + timedelta(duration)
                q= 'insert into booking VALUES (null,"{}","{}","{}","{}")'.format(self.memberId,bookId,time,new_date)
                cr.execute(q)
                result = cr.fetchall()
                print(result)

                self.booksalot = self.booksalloted+1
                q= 'update addmembership set booksalloted ="{}" where mId ="{}"'.format(self.booksalot,self.memberId)
                cr.execute(q)
                conn.commit()
                showinfo('book',f"Book issued\n Due Dtae:{new_date} ")


        elif self.membertype=="Student":
            q = 'select booksAllowed,duration from membershiptype where typeName = "{}"'.format("Student")
            cr.execute(q)
            result = cr.fetchall()
            print(result)

            x=[]
            for i in result:
                x.append(i[0])
                duration=i[1]
            if x[0]==self.booksalloted:
                showwarning("booking","Exceed limit ")
            else:
                new_date = datetime.today() + timedelta(duration)
                q= 'insert into booking VALUES (null,"{}","{}","{}","{}")'.format(self.memberId,bookId,time,new_date)
                cr.execute(q)
                result = cr.fetchall()
                print(result)

                self.booksalot = self.booksalloted+1
                q= 'update addmembership set booksalloted ="{}" where mId ="{}"'.format(self.booksalot,self.memberId)
                cr.execute(q)
                conn.commit()
                showinfo('book', f"Book issued\n Due Dtae:{new_date} ")

        elif self.membertype=="Teacher":

            q = 'select booksAllowed,duration from membershiptype where typeName = "{}"'.format("Teacher")
            cr.execute(q)
            result = cr.fetchall()
            print(result)

            x=[]
            for i in result:
                x.append(i[0])
                duration=i[1]
            if x[0]==self.booksalloted:
                showwarning("booking","Exceed limit ")
            else:
                new_date = datetime.today() + timedelta(duration)
                q= 'insert into booking VALUES (null,"{}","{}","{}","{}")'.format(self.memberId,bookId,time,new_date)
                cr.execute(q)
                result = cr.fetchall()
                print(result)

                self.booksalot = self.booksalloted+1
                q= 'update addmembership set booksalloted ="{}" where mId ="{}"'.format(self.booksalot,self.memberId)
                cr.execute(q)
                conn.commit()
                showinfo('book', f"Book issued\n Due Dtae:{new_date} ")


    def logout(self):
        self.root.destroy()










# student()