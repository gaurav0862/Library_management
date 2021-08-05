import time
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
from PIL import Image,ImageTk
import datetime
# import adminHome

class login:

    def __init__(self):

        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Login")
        self.img = (Image.open("image resources/img1.png"))
        self.resized_image = self.img.resize((500, 600), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas1 = Canvas(self.root, width=500, height=500)
        self.canvas1.place(x=0, y=0)
        self.root.resizable(0, 0)

        self.canvas1.create_image(0, 0, image=self.new_image, anchor="nw")

        self.var_1 = StringVar()
        self.var_2 = StringVar()
        # self.canvas1.create_text(100,35, text="Login",font=('Ink Free',50,"bold",))
        self.canvas1.create_text(50, 245, text="USER ID : ", font=('arial', 10, "bold"), fill="white")

        self.eme = Entry(self.root, textvariable=self.var_1)
        self.eme.place(x=90, y=235)
        self.canvas1.create_text(270, 245, text="PASSWORD : ", font=('arial', 10, "bold"), fill="white")
        self.eme_1 = Entry(self.root, textvariable=self.var_2, show='*')
        self.eme_1.place(x=320, y=235)
        self.btn = Button(self.root, text="LOGIN", command=self.login1)
        self.btn.place(x=225, y=300)
        # self.canvas1.create_text(245,275, text="Forgot password", font=('Helveticabold', 7))

        # self.new = Label(self.root, text="this is a test")
        # self.new.pack(side='bottom')
        # self.new.bind("<Button-1>", '')

        self.root.mainloop()

    def login1(self):

        conn = connect(host="127.0.0.1",user="root",password="",database="library_management")
        cr = conn.cursor()

        self.lgv = self.var_1.get()
        self.lgv_1 = self.var_2.get()

        if self.lgv == "" and self.lgv_1 == "":
            showinfo("Login", "Please provide id password")

        else:
            q = 'select * from adminmember where email="{}" and password="{}" '.format(self.lgv, self.lgv_1)
            cr.execute(q)
            self.result = cr.fetchone()
            print(self.result)
            if self.result == None:
                showinfo('Login', "Invalid Input")
            else:
                print(datetime.datetime.now())
                self.time_1 = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                print(self.time_1)
                q = 'update adminmember set lastLogin="{}" where email="{}"'.format(self.time_1, self.lgv)
                self.result = cr.execute(q)
                conn.commit()
                showinfo('Login', "Login Sucessfull")
                print("Login Sucessfull")
                self.root.destroy()
                # adminHome.demo()




obj=login()