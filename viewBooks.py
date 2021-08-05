from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class viewbook:

    def __init__(self):

        self.top = Toplevel()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.top.label_3 = Label(self.top, text="BOOKS", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,pady=20)
        self.top.title("View Products")
        self.top.waraper = LabelFrame(self.top, text="VIEW BOOKS")
        self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
        self.trv1 = Treeview(self.top.waraper, columns=(1, 2, 3, 4, 5,6,7,8,9), show="headings", height="5")
        self.trv1.pack(padx=10, pady=10)
        self.trv1.column("# 1",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 2",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 3",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 4",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 5",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 6",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 7",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 8",anchor=CENTER, stretch=NO, width=100)
        self.trv1.column("# 9",anchor=CENTER, stretch=NO, width=100)
        self.trv1.heading(1, text="Book ID")
        self.trv1.heading(2, text="Book Name")
        self.trv1.heading(3, text="Book Author")
        self.trv1.heading(4, text="Editor")
        self.trv1.heading(5, text="No. of topics")
        self.trv1.heading(6, text="Description")
        self.trv1.heading(7, text="ISBN")
        self.trv1.heading(8, text="Section")
        self.trv1.heading(9, text="Sub Section")
        self.trv1.bind("<Double-1>", self.show_details)
        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        q = 'select * from books'
        cr.execute(q)
        self.result = cr.fetchall()

        for i in self.trv1.get_children():
            self.trv1.delete(i)

        for i in self.result:
            self.trv1.insert("", END, value=i)

    def show_details(self, event):
            self.temp_data = self.trv1.item(self.trv1.focus())['values']
            self.top = Toplevel()
            self.main_frame=Frame(self.top)
            self.main_frame.pack(fill=BOTH,expand=1)

            self.my_canvas = Canvas(self.main_frame)
            self.my_canvas.pack(side=LEFT,fill=BOTH,expand=1)


            self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL,command=self.my_canvas.yview)
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.my_canvas.configure(yscrollcommand=self.scrollbar.set)
            self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

            self.second_frame = Frame(self.my_canvas)

            self.my_canvas.create_window((0,0,), window=self.second_frame,anchor='nw')
            # self.myscroll = Listbox(self.top, yscrollcommand=self.scrollbar.set)


            self.top.geometry('500x500')
            self.label_1 = Label(self.second_frame, text="Book ID ").pack(side=TOP, pady=10)
            self.em1 = Entry(self.second_frame)
            self.em1.insert(0, self.temp_data[0])
            self.em1.pack(side=TOP, pady=10)
            self.label_2 = Label(self.second_frame, text="Book Name ").pack(side=TOP, pady=10)
            self.em2 = Entry(self.second_frame)
            self.em2.insert(0, self.temp_data[1])
            self.em2.pack(side=TOP, pady=10)
            self.label_3 = Label(self.second_frame, text="Author ").pack(side=TOP, pady=10)
            self.em3 = Entry(self.second_frame)
            self.em3.insert(0, self.temp_data[2])
            self.em3.pack(side=TOP, pady=10)
            self.label_4 = Label(self.second_frame, text="Editor ").pack(side=TOP, pady=10)
            self.em4 = Entry(self.second_frame)
            self.em4.insert(0, self.temp_data[3])
            self.em4.pack(side=TOP, pady=10)
            Label(self.second_frame, text="No. of topics").pack(side=TOP, pady=10)
            self.em5 = Entry(self.second_frame)
            self.em5.insert(0, self.temp_data[4])
            self.em5.pack(side=TOP, pady=10)
            Label(self.second_frame, text=" Description").pack(side=TOP, pady=10)
            self.em6 = Entry(self.second_frame)
            self.em6.insert(0, self.temp_data[5])
            self.em6.pack(side=TOP, pady=10)
            Label(self.second_frame, text=" ISBN").pack(side=TOP, pady=10)
            self.em7 = Entry(self.second_frame)
            self.em7.insert(0, self.temp_data[6])
            self.em7.pack(side=TOP, pady=10)
            self.label_5 = Label(self.second_frame, text="Section").pack(side=TOP, pady=10)
            conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            q = 'select SectionName from section'
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchall()
            x = []
            for i in self.result:
                x.append(i[0])
            self.enl = Combobox(self.second_frame, values=x, state="readonly")
            print(self.enl)
            self.current = x.index(str(self.temp_data[7]))
            self.enl.current(self.current)
            self.enl.pack(side=TOP, pady=10)
            self.enl.config(state='readonly')
            self.enl.insert(0, self.temp_data[7])

            self.label_5 = Label(self.second_frame, text="Sub Section").pack(side=TOP, pady=10)
            conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            q = 'select subSectionname from subsection'
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchall()
            x = []
            for i in self.result:
                x.append(i[0])
            self.enl1 = Combobox(self.second_frame, values=x, state="readonly")
            print(self.enl)
            self.current = x.index(str(self.temp_data[8]))
            self.enl1.current(self.current)
            self.enl1.pack(side=TOP, pady=10)
            self.enl1.config(state='readonly')
            self.enl1.insert(0, self.temp_data[8])

            self.upbtn = Button(self.second_frame, text="update", command=self.newupdate)
            self.upbtn.pack()
            self.delbtn = Button(self.second_frame, text="Delete", command=self.delupdate)
            self.delbtn.pack()

            # self.myscroll.pack(side=LEFT, fill=BOTH)
            # self.scrollbar.config(command=self.myscroll.yview)

# --------------UPDATE EXISTING DATA--------------

    def newupdate(self):

            conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            q = 'update books set bookId="{}",bookName="{}",author="{}",editor="{}",numberOfTopics="{}",description="{}",ISBN="{}",SectionName="{}",subSectionname="{}" where bookId="{}"'.format(self.em1.get(), self.em2.get(),self.em3.get(),self.em4.get(),self.em5.get(),self.em6.get(),self.em7.get(),self.enl.get(),self.enl1.get(),self.em1.get())
            print(q)
            cr.execute(q)
            print(q)
            conn.commit()
            self.result = cr.fetchall()
            messagebox.showinfo("",f"Book ID {self.em1.get()} updated successfully ")

            q = 'select * from books'
            cr.execute(q)
            self.result = cr.fetchall()

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in self.result:
                self.trv1.insert("", END, value=i)
# -------DELETE ALL SELECTED DATA----------------

    def delupdate(self):

            conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
            cr = conn.cursor()
            q = 'delete from books where bookId="{}"'.format(self.em1.get)

            cr.execute(q)
            print(q)
            conn.commit()
            # cr = conn.cursor()
            q = 'select * from books'
            cr.execute(q)
            self.result = cr.fetchall()

            for i in self.trv1.get_children():
                self.trv1.delete(i)

            for i in self.result:
                self.trv1.insert("", END, value=i)
