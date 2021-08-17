from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *
from datetime import date


class issue:

    def __init__(self):
        self.top = Toplevel()
        self.top.title("Sections")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.top.label_3 = Label(self.top, text="Issued Books", font=("Constantia", "20", "italic", 'bold')).pack(side=TOP,
                                                                                                              pady=20)
        self.top.label_3 = Label(self.top, text="Search", font=("Constantia", "10", "italic", 'bold')).pack()
        self.search = Entry(self.top,width=25)
        self.search.pack()
        self.searchbutton = Button(self.top,text="Search",command=self.searchview)
        self.searchbutton.pack(pady=10)

        self.top.waraper = LabelFrame(self.top, text="Book Details")
        self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
        self.trv = Treeview(self.top.waraper, columns=(1,2,3,4,5,6,7,8), show="headings", height="5")
        self.trv.pack(padx=10, pady=50)
        self.trv.column("# 1", anchor=CENTER, stretch=NO, width=100)
        self.trv.column("# 2", anchor=CENTER, stretch=NO, width=100)
        self.trv.column("# 3", anchor=CENTER, stretch=NO, width=100)
        self.trv.column("# 4", anchor=CENTER, stretch=NO, width=100)
        self.trv.column("# 5", anchor=CENTER, stretch=NO, width=100)
        self.trv.column("# 6", anchor=CENTER, stretch=NO, width=100)
        self.trv.column("# 7", anchor=CENTER, stretch=NO, width=100)
        self.trv.column("# 8", anchor=CENTER, stretch=NO, width=100)

        self.trv.heading(1, text="Bookin ID")
        self.trv.heading(2, text="Member ID")
        self.trv.heading(3, text="Book ID")
        self.trv.heading(4, text="Date of issue")
        self.trv.heading(5, text="Due Date")
        self.trv.heading(6, text="Status")
        self.trv.heading(7, text="Return Date")
        self.trv.heading(8, text="Book Name")
        self.trv.bind("<Double-1>", self.updatestatus)



        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        q = 'select * from Booking '

        cr.execute(q)
        result = cr.fetchall()
        for i in result:
            self.bookid = i[2]
            self.bookingId=i[0]

        query = 'select bookName from books where bookId = "{}"'.format(self.bookid)
        cr.execute(query)
        result1 = cr.fetchone()
        x = []
        for i in result:
            y = list(i)
            y.append(result1[0])
            x.append(y)
            print(x)

        for i in self.trv.get_children():
            self.trv.delete(i)
        count = 0
        for i in x:
            self.trv.insert("", index=count, value=i)
            count += 1

    def searchview(self):

        searchValue=self.search.get()

        conn = connect(host="127.0.0.1", user="root", password="", database="library_management")
        cr = conn.cursor()
        q = 'select * from booking where bookingId = "{}" or memberId ="{}" or bookId="{}"'.format(searchValue,searchValue,searchValue)
        cr.execute(q)
        result2 = cr.fetchall()
        for i in result2:
            self.memberID=i[1]

        if result2 == ():
            showerror('Search', "No Data Found")

        else:
            self.new2 = self.bookid

            query = 'select bookName from books where bookId = "{}"'.format(self.bookid)
            cr.execute(query)
            result3 = cr.fetchone()
            x = []
            for i in result2:
                y = list(i)
                y.append(result3[0])
                x.append(y)

            for i in self.trv.get_children():
                self.trv.delete(i)
            count = 0

            for i in x:
                self.trv.insert("", index=count, value=i)
                count += 1

        self.trv.bind("<Double-1>",self.updatestatus)

    def updatestatus(self,event):

        self.temp_data = self.trv.item(self.trv.focus())['values']

        self.top = Toplevel()
        Label(self.top,text = "Update Book status",font=("Constantia", "20", "italic", 'bold'),pady=10).pack()
        self.top.geometry("500x500")
        self.p1 = PanedWindow(self.top)
        self.p1.pack()
        Label(self.p1, text="Booking ID: ").grid(row=0,column=0)
        self.BookinID = Entry(self.p1)
        self.BookinID.insert(0, self.temp_data[0])
        self.BookinID.config(state='readonly')
        self.BookinID.grid(row=0,column=1,pady=10)
        Label(self.p1, text="Member ID: ").grid(row=0,column=2,pady=10)
        self.MemberID = Entry(self.p1)
        self.MemberID.insert(0, self.temp_data[1])
        self.MemberID.config(state='readonly')
        self.MemberID.grid(row=0,column=3,pady=10)
        Label(self.p1, text="Book ID: ").grid(row=1,column=0,pady=10)
        self.BookID = Entry(self.p1)
        self.BookID.insert(0, self.temp_data[2])
        self.BookID.config(state='readonly')
        self.BookID.grid(row=1,column=1,pady=10)
        Label(self.p1, text="Issue Date: ").grid(row=1,column=2,pady=10)
        self.issue_Date= Entry(self.p1)
        self.issue_Date.insert(0, self.temp_data[3])
        self.issue_Date.config(state='readonly')
        self.issue_Date.grid(row=1,column=3,pady=10)
        Label(self.p1, text="Due Date : ").grid(row=2, column=0,pady=10)
        self.Due_Date = Entry(self.p1)
        self.Due_Date.insert(0, self.temp_data[4])
        self.Due_Date.config(state='readonly')
        self.Due_Date.grid(row=2, column=1,pady=10)
        Label(self.p1, text="status: ").grid(row=2, column=2,pady=10)
        self.enp_1 = ("Return", "Issue","Requested","Reject")
        self.status = self.enp_1.index(str(self.temp_data[5]).capitalize())
        self.enl = Combobox(self.p1, values=self.enp_1, state="readonly")
        self.enl.current(self.status)
        self.enl.grid(row=2, column=3,pady=10)
        self.enl.insert(0, self.temp_data[5])
        self.enl.config(state='readonly')
        Label(self.p1, text="Submit Date : ").grid(row=3, column=0,pady=10)
        self.submmitdate = Entry(self.p1)
        self.submmitdate.insert(0, self.temp_data[6])
        self.submmitdate.bind('<Double-1>', self.current_date)
        self.submmitdate.grid(row=3, column=1,pady=10)
        Button(self.p1,text="update",command = self.update,padx=13).grid(row=3,column=2,padx=10)


    def current_date(self,event):

        newdate = date.today()
        self.submmitdate.insert('0',newdate)
        self.submmitdate.config(state='readonly')
        print(newdate)

    def update(self):

        status = self.enl.get()

        if status == "Requested":
            pass

        elif status == "Reject":
            conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            q = 'update booking set status = "{}" , dateOfReturn = "{}" where bookingId = "{}"'.format("Rejected",self.submmitdate.get(),self.bookingId)
            print(q)
            cr.execute(q)
            conn.commit()

            showinfo('Issued book', "Book Rejected")



        elif status == "Issue":
                conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
                cr = conn.cursor()
                q = 'update booking set status = "{}" , dateOfReturn = "{}" where bookingId = "{}"'.format("issue",self.submmitdate.get() ,self.bookingId)
                print(q)
                cr.execute(q)

                q1= 'select booksalloted from addmembership where mID= "{}"'.format(self.memberID)
                cr.execute(q1)
                result = cr.fetchone()
                for i in result:
                    self.new1=i+1

                q2 ='update addmembership set booksalloted = "{}" where mId="{}"'.format(self.new1,self.memberID)
                cr.execute(q2)
                conn.commit()

                showinfo('Issued book',"Book Issued")

        elif status == "Return":

            conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            q = 'update booking set status = "{}" , dateOfReturn = "{}" where bookingId = "{}"'.format("Return",
                                                                                                       self.submmitdate.get(),
                                                                                                       self.bookingId)
            print(q)
            cr.execute(q)

            q1 = 'select booksalloted from addmembership where mID= "{}"'.format(self.memberID)
            cr.execute(q1)
            result = cr.fetchone()
            for i in result:
                self.new1 = i - 1

            q2 = 'update addmembership set booksalloted = "{}" where mId="{}"'.format(self.new1, self.memberID)
            cr.execute(q2)
            conn.commit()

            showinfo('Issued book', "Book Returned")



        else:
            self.top.destroy()
