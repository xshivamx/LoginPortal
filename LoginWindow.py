from tkinter import*
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
import pymysql

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")


        self.img=ImageTk.PhotoImage(file="Image/loginBG.jpg")
        bground =Label(self.root,image=self.img).place(x=0,y=0, relwidth=1, relheight=1)

        frame1= Frame(self.root,bg="white",bd=0).place(x=500,y=150, width=300, height=350)

        title = Label(frame1,text ="Login",font=("cambria",20,"bold"),bg="white", fg="grey").place(x=510,y=160)

        email= Label(frame1,text ="Username",font=("cambria",12,"bold"),bg="white", fg="grey").place(x=510,y=220)
        self.email = Entry(frame1, text="Enter Username", font=("cambria", 10), bg="light grey", fg="black")
        self.email.place(x=510,y=245)

        password = Label(frame1, text="Password", font=("cambria", 12, "bold"), bg="white", fg="grey").place(x=510,y=270)
        self.password = Entry(frame1, text="Enter password", font=("cambria", 10), bg="light grey", fg="black")
        self.password.place(x=510, y=295)

        reg_btn=Button(frame1,text="Register For New Account?",font=("cambria",10),bg="white",fg="red",bd=0,command=self.register_window,cursor="hand2").place(x=510, y=330)
        forget_btn = Button(frame1,command=self.forget_window,font=("cambria",10),text="Forget Password",bg="white",bd=0,fg="red",cursor='hand2').place(x=670,y=330)

        self.log_btn=ImageTk.PhotoImage(file="image/login.png")
        log_btn = Button(frame1,image=self.log_btn,bd=0,cursor="hand2",command=self.login).place(x=510, y=350)




    def forget_window(self):
        if self.email.get()=="":
            messagebox.showerror("error","Please enter a Valid email address", parent=self.root)
        else:
            try:
                con= pymysql.connect(host='localhost', user='root', password='',database="Login")
                cur= con.cursor()
                cur.execute("select * from Login where email=%s",(self.email.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error", "Please enter Correct email address to reset your password", parent=self.root)
                else:
                    self.root2 = Toplevel()
                    self.root2.title("Reset Password")
                    self.root2.geometry("300x300+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    title = Label(self.root2, text="Reset Password", font=("cambria", 20, "bold"), bg="white").place(x=70, y=15)

                    quest = Label(self.root2, text="Security Question", font=("cambria", 12, "bold"), bg='white',fg='grey').place(x=70, y=55)
                    self.quest = ttk.Combobox(self.root2, state="readonly")
                    self.quest["value"] = ("--SELECT--", "Your Birth Place", "Your First Pet", "Your Favourite Anime")
                    self.quest.place(x=70, y=80)
                    self.quest.current(0)

                    answer = Label(self.root2, text="Answer", font=('cambria', 12, "bold"), bg="white",fg="grey").place(x=70, y=105)
                    self.answer = Entry(self.root2, font=("cambria", 10), bg="light grey")
                    self.answer.place(x=70, y=130)

                    New_pwd = Label(self.root2, text="New Password", font=('cambria', 12, "bold"), bg="white",fg="grey").place(x=70, y=155)
                    self.new_pwd = Entry(self.root2, font=("cambria", 10), bg="light grey")
                    self.new_pwd.place(x=70, y=180)

                    confirm = Button(self.root2, text="Confirm", command= self.cnf_pwd,font=("cambria", 12), cursor="hand2", bg="Green",fg="white").place(x=70, y=220)

            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

    def cnf_pwd(self):
        if self.quest.get()=="--SELECT--" or self.answer.get()=="" or self.new_pwd.get()=="":
            messagebox.showerror("error", "All feilds are required ", parent=self.root2)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database="Login")
                cur = con.cursor()
                cur.execute("select * from Login where email=%s and quest=%s and answer=%s", (self.email.get(),self.quest.get(),self.answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("error", "Please Choose the Correct Security Q/A to reset",
                                         parent=self.root2)
                else:
                    cur.execute("update login set password=%s where email=%s",
                                (self.new_pwd.get(),self.email.get()))
                    con.commit()
                    con.close()
                    messagebox.showerror("Success", "Your password Successfully changed.",
                                         parent=self.root2)

                    self.reset()
                    self.root2.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root2)

    def reset(self):
        self.email.delete(0,END)
        self.password.delete(0, END)
        self.quest.delete(0)
        self.answer.delete(0, END)
        self.new_pwd.delete(0, END)

    def register_window(self):
        self.root.destroy()
        import registration


    def login(self):
        if self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","Please Enter Username and Password",parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="Login")
                cur = con.cursor()

                cur.execute("select * from Login where email=%s and password=%s",(self.email.get(),self.password.get()) )
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error", "Invalid Username & password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Login Sucessfully!", parent=self.root)
                    self.root.destroy()
                    import Student

            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)


root = Tk()
log = Login_window(root)
root.mainloop()