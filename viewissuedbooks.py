from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *


class issue:

    def __init__(self,id):
        self.memberId = id
        self.top = Toplevel()
        self.top.title("Sections")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.top.label_3 = Label(self.top, text="Issued Books", font=("Constantia", "20", "italic", 'bold')).pack(side=TOP,
                                                                                                              pady=20)

        self.top.waraper = LabelFrame(self.top, text="Book Details")
        self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
        self.trv = Treeview(self.top.waraper, columns=(1,2,3,4,5), show="headings", height="5")
        self.trv.pack(padx=10, pady=50)
        self.trv.heading(1, text="Iusse ID")
        self.trv.heading(2, text="Book ID")
        self.trv.heading(3, text="Date of issue")
        self.trv.heading(4, text="Due Date")
        self.trv.heading(5, text="Book Name")

        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        q = 'select bookingId,bookId,dateOfBooking,dateOfRelease from Booking where memberId = "{}"'.format(self.memberId)

        cr.execute(q)
        result = cr.fetchall()
        for i in result:
            bookid=i[1]
        query = 'select bookName from books where bookId = "{}"'.format(bookid)
        cr.execute(query)
        result1 = cr.fetchone()
        x = []
        for i in result:
            y = list(i)
            y.append(result1[0])
            x.append(y)

        for i in self.trv.get_children():
            self.trv.delete(i)
        count = 0
        for i in x:
            self.trv.insert("", index=count, value=i)
            count += 1
