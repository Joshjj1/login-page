from cProfile import label
from cgitb import text
from email.mime import image
from tkinter import *
from tkinter import font,messagebox
from turtle import title        #using python gui tkinter
from PIL import ImageTk,Image        #using pillow to use images

class login_system:
    def __init__(self,root):
        self.root=root 
        self.root.title("Login page")
        self.root.geometry("1350x700+0+0")
 #========== All images============
        self.bg_icon=ImageTk.PhotoImage(file="C:/Users/joshj/Desktop/python 2/proj1/bkimage2.jpg") 
       
        userimg=(Image.open("C:/Users/joshj/Desktop/python 2/proj1/username.png"))  
        resizeuser = userimg.resize((50, 50), Image.ANTIALIAS)
        self.user_icon=ImageTk.PhotoImage(resizeuser) 
       
        passimg=(Image.open("C:/Users/joshj/Desktop/python 2/proj1/password.jpg"))
        resizepass= passimg.resize((50,50),Image.ANTIALIAS)
        self.pass_icon=ImageTk.PhotoImage(resizepass)
       
        logoimg=(Image.open("C:/Users/joshj/Desktop/python 2/proj1/logo.png")) 
        resizelogo = logoimg.resize((100, 100), Image.ANTIALIAS)
        self.logo_icon=ImageTk.PhotoImage(resizelogo) 
        #===== login labels and texts ==========

        self.uname=StringVar()
        self.Pass=StringVar()

        bg_lb1=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Login system", font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)        
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")  
        Login_Frame.place(x=400,y=150)

        logolb1=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",10,"bold"),bg="white").grid(row=1,column=0,padx=10,pady=20)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",10,"bold"),bg="white").grid(row=2,column=0,padx=10,pady=20)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.Pass,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
        
        btn_log=Button(Login_Frame,text="Log in",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10) 
        

    def login(self):
        if self.uname.get()=="" or self.Pass.get()=="":
            messagebox.showerror("Error"," All fields are required")
        elif self.uname.get()=="JOSH" and self.Pass.get()=="Hello World":
            messagebox.showinfo("Successful",f"Welcome {self.uname.get()}")
        else: 
            messagebox.showerror("Error","Invalid Username or Password")


root=Tk() 
obj=login_system(root)
root.mainloop()
