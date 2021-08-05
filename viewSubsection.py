from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class viewsubsec:

     def __init__(self):
                self.top=Toplevel()
                self.top.title("Sections")
                self.top.label_3 = Label(self.top, text="Sub Sections",font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,pady=20)
                self.top.label4 = Label(self.top, text="Double click to delete value", font=("Constantia", "10", 'bold')).pack(side="bottom", pady=20)
                self.top.waraper = LabelFrame(self.top,text="Sub Sections Details")
                self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
                self.trv = Treeview(self.top.waraper, columns=(1, 2), show="headings", height="5")
                self.trv.pack(padx=10, pady=50)
                self.trv.heading(1, text="Sub Sections")
                self.trv.heading(2, text="Section")
                self.trv.bind("<Double-1>", self.delcat)
                conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
                cr = conn.cursor()
                q = 'select * from subsection'
                cr.execute(q)
                self.result = cr.fetchall()

                for i in self.trv.get_children():
                    self.trv.delete(i)

                for i in self.result:
                    self.trv.insert("", END, value=i)



#------------------Show Details---------------------------


     def delcat(self,event):

                self.temp_data = self.trv.item(self.trv.focus())['values']


                self.new= messagebox.askquestion("Delete", f"Do You want to delete {self.temp_data[0]} Section ? ")
                if self.new == "yes":
                    conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
                    cr = conn.cursor()
                    q= 'delete from section where sectionName = "{}"'.format(self.temp_data[0])
                    print(q)
                    cr.execute(q)
                    conn.commit()
                    self.result = cr.fetchone()
                else:
                    pass