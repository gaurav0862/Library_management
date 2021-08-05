from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *



class addpro:

    def sub(self,event):


        # Label(self.top, text="Sub Section :: ",font=("arial", "10", 'bold')).place(x=580, y=500)
        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        q = 'select * from subsection where SectionName="{}"'.format(self.enl1.get())
        cr.execute(q)
        conn.commit()
        print(q)

        self.result = cr.fetchall()
        y1 = []
        for j in self.result:
            y1.append(j[0])
            self.enl2.config(values=y1)

        # self.enl2 = Combobox(self.top, values=y)
        # self.enl2.place(x=690, y=500)
        #
        # self.Button1 = Button(self.top, text='ADD', command=self.newpro,padx=5,width=12)
        # self.Button1.place(x=855, y=497)


    def __init__(self):
        global y1
        self.top = Toplevel()
        self.top.title("ADD BOOK")
        # self.top.state("zoomed")
        self.top.geometry("1366x700+0+0")
        self.top.resizable(0, 0)
        self.top.label_5 = Label(self.top, text="ADD BOOK", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,                                                                                                        pady=20)
        Label(self.top, text="Book Name :: ",font=("arial", "10", 'bold')).place(x=300, y=160)
        self.en2 = Entry(self.top)
        self.en2.place(x=400, y=160)
        Label(self.top, text="Author :: ",font=("arial", "10", 'bold')).place(x=550, y=160)
        self.en3 = Entry(self.top)
        self.en3.place(x=620, y=160)
        Label(self.top, text="Editor :: ",font=("arial", "10", 'bold')).place(x=770, y=160)
        self.en4 = Entry(self.top)
        self.en4.place(x=840, y=160)
        Label(self.top, text="Number of Topics :: ",font=("arial", "10", 'bold')).place(x=300, y=260)
        self.en5 = Entry(self.top)
        self.en5.place(x=440, y=260)
        Label(self.top, text="Description :: ",font=("arial", "10", 'bold')).place(x=300, y=360)
        self.en6 = Text(self.top, height=5, width=47)
        self.en6.place(x=440, y=360)
        Label(self.top, text="ISBN :: ",font=("arial", "10", 'bold')).place(x=580, y=260)
        self.en7 = Entry(self.top)
        self.en7.place(x=650, y=260)
        Label(self.top, text="Section Name :: ",font=("arial", "10", 'bold')).place(x=300, y=500)
        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()
        q = 'select sectionName from section'
        cr.execute(q)
        conn.commit()
        self.result = cr.fetchall()
        x = []
        for i in self.result:
            x.append(i[0])
        self.enl1 = Combobox(self.top, values=x, state='readonly')
        self.enl1.bind('<<ComboboxSelected>>', self.sub )
        self.enl1.place(x=420, y=500)

        Label(self.top, text="Sub Section :: ", font=("arial", "10", 'bold')).place(x=580, y=500)
        self.enl2 = Combobox(self.top, values=(),state='readonly')
        self.enl2.place(x=690, y=500)



        self.Button1 = Button(self.top, text='ADD', command=self.newpro, padx=5, width=12)
        self.Button1.place(x=855, y=497)



    def newpro(self):
        self.pdes = self.en6.get(1.0, END)


        conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
        cr = conn.cursor()

        if self.en2.get()=="" or self.en3.get()=="" or self.en4.get()=="" or  self.en5.get()=="" or self.pdes=="" or self.en7.get()=="" or self.enl1.get()=="" or self.enl2.get()=="":
            showinfo("ADD BOOK","Provide valid inputs")
        else:

            try:
                self.new = int(self.en5.get())

                q = 'insert into books values ("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format("null", self.en2.get(), self.en3.get(),self.en4.get(),self.en5.get(),self.pdes,self.en7.get(),self.enl1.get(),self.enl2.get(),)
                cr.execute(q)
                print(q)
                conn.commit()

                self.result = cr.fetchall()
                self.top.destroy()
                showinfo('Add BOOK', "Book Added Sucessfully")

            except:
                showinfo("","Please input number")
                self.top.destroy()