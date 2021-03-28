from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
#ImageTk helps to deal with image file in python
import pymysql

class register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("3840x2160+0+0")
        self.root.config(bg="white")
#=====setting Bg=======
        self.bg = ImageTk.PhotoImage(file="Image/tra.jpg")
        bg = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=2,relheight=2)
# =====setting side Image over BG=======
        self.left = ImageTk.PhotoImage(file="Image/luffy.jpg")
        left = Label(self.root, image=self.left).place(x=100, y=200, width=621, height=350)

#registration frame
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=721, y=200, width=400,height=350)

        title=Label(frame1,text="Register Here",font=('cambria',20,"bold"),bg="white", fg="black").place(x=20,y=10)
#Row 1
        #self.fname=StringVar() == texvariable="self.fname"
        f_name=Label(frame1, text="First Name", font=("cambria", 10, "bold"), bg="white", fg="grey").place(x=20,y=60)
        self.fname =Entry(frame1,font=("cambria",10),bg="light grey" )
        self.fname.place(x=20, y=80, width=150)

        l_name=Label(frame1,text="Last Name", font=("cambria", 10, "bold"),bg="white", fg = "grey").place(x=200, y=60)
        self.lname=Entry(frame1,font=("cambria",10),bg="light grey")
        self.lname.place(x=200,y=80, width="150")

#Row 2
        contact = Label(frame1, text="Contact", font=("cambria", 10, "bold"), bg="white", fg="grey").place(x=20, y=110)
        self.contact = Entry(frame1, font=("cambria", 10), bg="light grey")
        self.contact.place(x=20, y=130, width=150)

        email = Label(frame1, text="Email", font=("cambria", 10, "bold"), bg="white", fg="grey").place(x=200, y=110)
        self.email = Entry(frame1, font=("cambria", 10), bg="light grey")
        self.email.place(x=200, y=130, width="150")

#Row 3
        quest = Label(frame1,text="Security Question",font=("Cambria",10 ,"bold"),bg="white",fg="grey").place(x=20,y=160)
        self.quest = ttk.Combobox(frame1, font=("cambria", 8),state="readonly")
        self.quest["values"]=("--SELECT--","Your Birth Place","Your First Pet", "Your Favourite Anime")
        self.quest.place(x=20, y=180, width="150")
        self.quest.current(0)

        answer = Label(frame1,text="Answer",font=('cambria',10,"bold"),bg="white", fg="grey").place(x=200, y=160)
        self.answer = Entry(frame1, font=("cambria", 10), bg="light grey")
        self.answer.place(x=200, y=180, width="150")

#Row 4
        password = Label(frame1, text="Password",font=("cambria", 10, "bold"), bg="white", fg="grey").place(x=20, y=210)
        self.password = Entry(frame1, font=("cambria", 10), bg="light grey")
        self.password.place(x=20, y=230, width=150)

        cnf_pwd = Label(frame1, text="Confirm Password", font=("cambria", 10, "bold"), bg="white", fg="grey").place(x=200, y=210)
        self.cnf_pwd = Entry(frame1, font=("cambria", 10), bg="light grey")
        self.cnf_pwd.place(x=200, y=230, width="150")

#terms
        self.var_check=IntVar()
        check=Checkbutton(frame1, text="I Agree Above Terms.",onvalue=1,offvalue=0,variable=self.var_check,font=("cambria",10,"bold"),bg="white",fg="grey").place(x=20, y=260)


        self.btn=ImageTk.PhotoImage(file="Image/register.png")
        btn=Button(frame1, image=self.btn,bd=0, cursor="hand2",command=self.register_data).place(x=20, y=300)

        sign_up=Button(self.root,text="Login",font=("cambria",10), bg="Black", fg="white", bd=0,command=self.login_window, cursor="hand2").place(x=120, y=500,width=80)

    def login_window(self):
        self.root.destroy()
        import LoginWindow

#defining a funciton to clear the class:
    def clear(self):
        self.fname.delete(0,END)
        self.lname.delete(0,END)
        self.contact.delete(0,END)
        self.email.delete(0,END)
        self.quest.current(0)
        self.answer.delete(0,END)
        self.password.delete(0,END)
        self.cnf_pwd.delete(0,END)


    def register_data(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.contact.get()=="" or self.email.get()=="" or self.quest.get()=="--SELECT--" or self.answer.get()=="" or self.password.get()=="" or self.cnf_pwd.get()=="":
            messagebox.showerror("error","All Feild Required",parent=self.root)


        elif self.password.get() != self.cnf_pwd.get():
            messagebox.showerror("error", "Please Enter Correct Password", parent=self.root)

        elif self.var_check.get()==0:
            messagebox.showerror("error", "Please Agree The Terms.", parent=self.root)

        else:
            try:
                #connecting our database/staring connection
                con = pymysql.connect(host="localhost", user="root", password="",database="Login")
                cur = con.cursor()
                #queries select& insert
                cur.execute("select * from Login where email=%s",self.email.get())
                row = cur.fetchone()
                cur.execute("select * from Login where contact=%s", self.contact.get())
                num = cur.fetchone()
                #print(row)
                if row != None:
                    messagebox.showerror("Error", "Email already existed.", parent=self.root)
                elif num!= None:
                    messagebox.showerror("error","Number already exist.",parent=self.root)
                else:
                    cur.execute("insert into Login(fname,lname,contact,email,quest,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (
                        self.fname.get(),
                        self.lname.get(),
                        self.contact.get(),
                        self.email.get(),
                        self.quest.get(),
                        self.answer.get(),
                        self.password.get()
                        ))
                    con.commit() #it will save our details in database.
                    con.close() #closes our connection
                    messagebox.showinfo("Success", "Registration Successful!!", parent=self.root)
                    self.clear()
            except Exception as e:
                messagebox.showerror("error", f"error due to: {str(e)}", parent=self.root)


root = Tk()
reg = register(root)
root.mainloop()