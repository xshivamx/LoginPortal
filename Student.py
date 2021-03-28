from tkinter import*
from tkinter import ttk,messagebox
import pymysql

class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        title=Label(self.root,text="Student Management System",font=("Lucida Handwriting",25,"bold"),bg="#00e6e6"
                    ,fg="White",bd=5,relief=RIDGE)
        title.pack(side=TOP,fill=X)

#-------------Variables---------
        self.roll_var=StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()


        self.search_by_var= StringVar()
        self.txt_search_var = StringVar()


#----------Frame 1-------------
        frame1 = Frame(self.root,bg="#00e6e6",bd=4,relief=RIDGE)
        frame1.place(x=50, y= 75, width=450, height= 600)

        f_title=Label(frame1,text="Student Registration",font=("Cambria",20,"bold"),bg="#00e6e6", fg="white").grid(row=0,columnspan=2,pady=10)

        f_roll = Label(frame1, text="Roll No:", font=("Cambria", 15, "bold"),bg="#00e6e6", fg="white").grid(row=1, column=0,padx=10,pady=10, sticky="w")
        txt_roll = Entry(frame1,textvariable=self.roll_var, font=("Cambria", 12),bd=1,relief=RIDGE).grid(row=1, column=1, padx=10, pady=10, sticky="w")

        f_name = Label(frame1, text="Name:", font=("Cambria", 15, "bold"), bg="#00e6e6", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        txt_name= Entry(frame1,textvariable=self.name_var, font=("Cambria", 12), bd=1, relief=RIDGE).grid(row=2, column=1, padx=10, pady=10, sticky="w")

        f_email = Label(frame1, text="Email:", font=("Cambria", 15, "bold"), bg="#00e6e6", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        txt_email = Entry(frame1,textvariable=self.email_var, font=("Cambria", 12), bd=1, relief=RIDGE).grid(row=3, column=1, padx=10, pady=10, sticky="w")

        f_gender = Label(frame1, text="Gender:", font=("Cambria", 15, "bold"), bg="#00e6e6", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")

        txt_gender = ttk.Combobox(frame1,textvariable=self.gender_var, font=("Cambria", 11),state="readonly")
        txt_gender["values"]=("Male","Female","others")
        txt_gender.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        #txt_gender.current(0)

        f_contact = Label(frame1,text="Contact:", font=("Cambria", 15, "bold"), bg="#00e6e6", fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        txt_contact = Entry(frame1, textvariable=self.contact_var,font=("Cambria", 12), bd=1, relief=RIDGE).grid(row=5, column=1, padx=10, pady=10, sticky="w")

        f_dob = Label(frame1, text="D.O.B:", font=("Cambria", 15, "bold"), bg="#00e6e6", fg="white").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        txt_dob = Entry(frame1,textvariable=self.dob_var, font=("Cambria", 12), bd=1, relief=RIDGE).grid(row=6, column=1, padx=10, pady=10, sticky="w")

        f_address = Label(frame1, text="Address:", font=("Cambria", 15, "bold"), bg="#00e6e6", fg="white").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.txt_address = Text(frame1, width=26, height=5,font=("Cambria", 10), bd=1, relief=RIDGE)
        self.txt_address.grid(row=7, column=1, padx=10, pady=10, sticky="w")

#----------Button for frame 1--------------
        btn=Frame(frame1,bg="#00e6e6",bd=4,relief=RIDGE)
        btn.place(x=10,y=480,width=420,height=60)

        add = Button(btn,text="Add", command=self.add_student, width=8, font=("Cambria", 11,"bold"),bg="white", cursor="hand2" ,bd=2, relief=RIDGE).grid(row=0,column=0,padx=10,pady=15)

        update= Button(btn, text="Update",command=self.update, width=8, font=("Cambria", 11,"bold"),bg="white", cursor="hand2", bd=2, relief=RIDGE).grid(row=0, column=1, padx=10, pady=15)

        delete = Button(btn, text="Delete",command=self.delete, width=8, font=("Cambria", 11,"bold"),bg="white", cursor="hand2", bd=2, relief=RIDGE).grid(row=0, column=2, padx=10, pady=15)

        clear = Button(btn,command=self.clear, text="Clear", width=8, font=("Cambria", 11,"bold"),bg="white", cursor="hand2", bd=2, relief=RIDGE).grid(row=0, column=3, padx=10, pady=15)

#----------Frame 2-------------
        frame2 = Frame(self.root, bg="#00e6e6", bd=4, relief=RIDGE)
        frame2.place(x=550, y=75, width=750, height=600)

        f_title= Label(frame2,text="Search by:", font=("Cambria", 15, "bold"),bg="#00e6e6", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        search_by = ttk.Combobox(frame2,textvariable=self.search_by_var, font=("Cambria", 11), state="readonly")
        search_by["values"] = ("roll", "name", "email")
        search_by.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        txt_search = Entry(frame2, textvariable=self.txt_search_var, font=("Cambria", 12), bd=1, relief=RIDGE).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        search = Button(frame2,command=self.search, text="Search", width=8, font=("Cambria", 11,"bold"),bg="white", cursor="hand2", bd=2, relief=RIDGE).grid(row=0, column=3, padx=10, pady=15)

        Show = Button(frame2, command=self.fetch,text="Show all", width=8, font=("Cambria", 11,"bold"),bg="white", cursor="hand2", bd=2, relief=RIDGE).grid(row=0, column=4, padx=10, pady=15)

#--------------Table frame------------

        table=Frame(frame2,bd=4, relief=RIDGE,bg="#00e6e6")
        table.place(x=20,y=70,width=700,height=500)

        scroll_x=Scrollbar(table,orient=HORIZONTAL)#scrollbars
        scroll_y=Scrollbar(table,orient=VERTICAL)
#----------------create table----------------
        self.student_table=ttk.Treeview(table,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)#place's scroll bar
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

#-----------------headings for User----------------
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")

        self.student_table['show']='headings'#because of this it wont show empty column

        self.student_table.column("roll",width=80)
        self.student_table.column("name", width=120)
        self.student_table.column("email", width=120)
        self.student_table.column("gender", width=80)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=150)

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch()


    def add_student(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="loginstudent")
        cur=con.cursor()
        cur.execute("insert into student(roll,name,email,gender,contact,dob,address) values(%s,%s,%s,%s,%s,%s,%s)",(
                self.roll_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0',END)

            ))
        con.commit()
        self.fetch()
        self.clear()
        con.close()

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="loginstudent")
        cur = con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s",(

            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_address.get('1.0', END),
            self.roll_var.get()

        ))
        con.commit()
        self.fetch()
        self.clear()
        con.close()

    def clear(self):
        self.roll_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete('1.0', END)

    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="loginstudent")
        cur=con.cursor()
        cur.execute("delete from student where roll=%s",self.roll_var.get())
        con.commit()

        self.fetch()
        self.clear()
        con.close()

    def fetch(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="loginstudent")
        cur = con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,value=row)
            con.commit()
        con.close()

    def search(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="loginstudent")
        cur=con.cursor()
        cur.execute("select * from student where " + str(self.search_by_var.get()) + " LIKE '%" + str(self.txt_search_var.get()) + "%'")

        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, value=row)
            con.commit()
        con.close()
        
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content["values"]
        self.roll_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert( END,row[6])

root = Tk()
object = student(root)
root.mainloop()