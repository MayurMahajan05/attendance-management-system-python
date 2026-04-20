# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os

# class Login:
#     def __init__(self,root):
#         self.root= root
#         self.root.title("Login System")
#         self.root.geometry("1550x800+0+0")

#         # bg image
#         img_path = os.path.join(os.path.dirname(__file__), "college_images", "bg.jpg")
#         img = Image.open(img_path)
#         img = img.resize((1530, 800), Image.LANCZOS)

#         self.photoimg = ImageTk.PhotoImage(img)
#         bg_img = Label(self.root, image=self.photoimg)
#         bg_img.place(x=0, y=0, relheight=1,relwidth=1)

#         # frame
#         frame = Frame(self.root,bg="black")
#         frame.place(x=610,y=170,width=340,height=430)

#         # img
#         img_path1 = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
#         img1 = Image.open(img_path1)
#         img1 = img1.resize((90, 90), Image.LANCZOS)

#         self.photoimg1 = ImageTk.PhotoImage(img1)
#         f_lbl1 = Label(self.root, image=self.photoimg1)
#         f_lbl1.place(x=730, y=170, width=90, height=90)

#         get_str=Label(frame,text="get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
#         get_str.place(x=95,y=85)

#         # Label
#         username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
#         username.place(x=70,y=125)

#         self.txtuser = Entry(frame,font=("times new roman",15,"bold"))
#         self.txtuser.place(x=40,y=180,width=270)

#         password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
#         password.place(x=70,y=225)

#         self.txtpass = Entry(frame,font=("times new roman",15,"bold"),show="*")
#         self.txtpass.place(x=40,y=250,width=270)

#         # Icon Images

#         img_path2 = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
#         img2 = Image.open(img_path2)
#         img2 = img2.resize((25,25), Image.LANCZOS)

#         self.photoimg2 = ImageTk.PhotoImage(img2)
#         f_lbl2 = Label( image=self.photoimg2 , bg="black",borderwidth=0)
#         f_lbl2.place(x=650, y=323, width=25, height=25)

#         img_path3 = os.path.join(os.path.dirname(__file__), "college_images", "lock-512.png")
#         img3 = Image.open(img_path3)
#         img3 = img3.resize((25,25), Image.LANCZOS)

#         self.photoimg3 = ImageTk.PhotoImage(img3)
#         f_lbl3 = Label( image=self.photoimg3 , bg="black",borderwidth=0)
#         f_lbl3.place(x=650, y=395, width=25, height=25)


#         # Login Button
#         login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE,bg="black", fg="white",activebackground="black",activeforeground="white")
#         login_btn.place(x=110,y=300,width=120,height=35)

#         # register button
#         register_btn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"),borderwidth=0, relief=RIDGE,bg="black", fg="white",activebackground="black",activeforeground="white")
#         register_btn.place(x=15,y=350,width=160)

#         # forget button
#         forgot_pass_btn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),borderwidth=0, relief=RIDGE,bg="black", fg="white",activebackground="black",activeforeground="white")
#         forgot_pass_btn.place(x=10,y=370,width=160)


#     # ========= Login function ================

#     def login(self):
#         if self.txtuser.get() =="" or self.txtpass.get()=="":
#             messagebox.showerror("Error","All filed required")
#         elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
#             messagebox.showinfo("Success","welcome to codewithkiran channel please subscribe to my channel")
#         else:
#             messagebox.showerror("Invalid","invalid username and password")




# if __name__ == "__main__":
#     root=Tk()
#     obj=Login(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk
import random,os,tempfile
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import smtplib as s
from pdf_mail import sendpdf
from time import strftime
from main import Face_Recognition_System

def main():
   win=Tk()
   app=Login_Window(win)
   win.mainloop()



class Login_Window:
    def __init__(self,root):
       self.root=root
       self.root.title("Login")
       self.root.geometry("1550x800+0+0")

       # Dynamic Image Path
       img_path = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
       img = Image.open(img_path)
       img = img.resize((1550,800), Image.LANCZOS)
       self.bg = ImageTk.PhotoImage(img)

       lbl_bg=Label(self.root,image=self.bg)
       lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

       self.new_window = None

       frame=Frame(self.root,bg='black')
       frame.place(x=610,y=170,width=340,height=450)

       img_path1 = os.path.join(os.path.dirname(__file__), "college_images", "LoginIconAppl.png")
       img1 = Image.open(img_path1)
       img1 = img1.resize((100,100),Image.LANCZOS)
       self.photoimg1 = ImageTk.PhotoImage(img1)

       lblimg1=Label(image=self.photoimg1,borderwidth=0,bg="black")
       lblimg1.place(x=730,y=175,width=100,height=100)


       get_str=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"),fg="white",bg="black")
       get_str.place(x=70,y=100)

       username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
       username.place(x=70,y=155)

       self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
       self.txtuser.place(x=40,y=180,width=270)

       password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
       password.place(x=70,y=225)

       self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
       self.txtpass.place(x=40,y=250,width=270)

       img_path2 = os.path.join(os.path.dirname(__file__), "college_images", "LoginIconAppl.png")
       img2 = Image.open(img_path2)
       img2 = img2.resize((25,25),Image.LANCZOS)
       self.photoimg2 = ImageTk.PhotoImage(img2)

       lblimg2=Label(image=self.photoimg2,borderwidth=0,bg="black")
       lblimg2.place(x=650,y=323,width=25,height=25)

       img_path3 = os.path.join(os.path.dirname(__file__), "college_images", "lock-512.png")
       img3 = Image.open(img_path3)
       img3 = img3.resize((25,25),Image.LANCZOS)
       self.photoimg3 = ImageTk.PhotoImage(img3)

       lblimg3=Label(image=self.photoimg3,borderwidth=0,bg="black")
       lblimg3.place(x=650,y=394,width=25,height=25)

       loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",10,"bold"),
                       bd=3,relief=RIDGE,fg="white",bg="red",
                       activeforeground="white",activebackground="red")
       loginbtn.place(x=110,y=300,width=120,height=35)

       registerbtn=Button(frame,text="New User Register",command=self.register_window,
                          font=("times new roman",10,"bold"),
                          borderwidth=0,fg="white",bg="black",
                          activeforeground="white",activebackground="black")
       registerbtn.place(x=15,y=350,width=160)

       foregtpasswordbtn=Button(frame,text="Forget Password",
                                command=self.forgot_password_window,
                                font=("times new roman",10,"bold"),
                                borderwidth=0,fg="white",bg="black",
                                activeforeground="white",activebackground="black")
       foregtpasswordbtn.place(x=10,y=370,width=160)

    def register_window(self):
      self.new_window=Toplevel(self.root)
      self.app=Register(self.new_window)



    def login(self):
      try:
       if self.txtuser.get()=="" or self.txtpass.get()=="":
        messagebox.showerror("Error","all field required")
       elif self.txtuser.get()=="Pranayjha123" and self.txtpass.get()=="Pranayjha@123":
        messagebox.showinfo("Success","welcome to face recog software")
       else :
        conn=mysql.connector.connect(host="localhost",username="root",password="Bunty@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM register where email=%s and password=%s",( 
                                                                                      self.txtuser.get(),
                                                                                      self.txtpass.get()
                                                                                      ))
        row=my_cursor.fetchone()
        if row==None:
           messagebox.showerror("Error","Invalid Username & Password")
        else:
           open_main=messagebox.askyesno("YesNo","Access only admin")
           if open_main>0:
              self.new_window=Toplevel(self.new_window)
              self.app=Face_Recognition_System(self.new_window)  # face recog should be mentioned here
           else:
              if not open_main:
                 return
        conn.commit()
        conn.close()
      except Exception as e :
         messagebox.showerror("Error",str(e))


        #  ============ reset password ===========

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
          messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security.get()=="":
          messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
          messagebox.showerror("Error","please enter the new password",parent=self.root2)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Bunty@123",database="face_recognizer")
           my_cursor=conn.cursor()
           query=("SELECT * FROM register where email=%s and securityQ=%s and securityA=%s")
           value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row==None:
              messagebox.showerror("Error","please enter the correct answer",parent=self.root2)
           else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()


    def forgot_password_window(self):
         if self.txtuser.get()=="":
             messagebox.showerror("Error","please enter Email address to Reset Password")
         else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Bunty@123",database="face_recognizer")
           my_cursor=conn.cursor()
           query=("SELECT * FROM register where email=%s")
           value=(self.txtuser.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()

           if row==None:
               messagebox.showerror("Error","Please enter the valid User name")
           else:
               conn.close()
               self.root2=Toplevel()
               self.root2.title("Forgot Password")
               self.root2.geometry("340x450+610+170")

               security_Q=Label(self.root2,text="Select Security Question",
                                font=("times new roman",15,"bold"),bg="white",fg="black")
               security_Q.place(x=50,y=80)

               self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
               self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
               self.combo_security_Q.place(x=50,y=110,width=250)
               self.combo_security_Q.current(0)

               security_A=Label(self.root2,text="Security Answer",
                                font=("times new roman",15,"bold"),bg="white",fg="black")
               security_A.place(x=50,y=150)

               self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
               self.txt_security.place(x=50,y=180,width=250)

               new_password=Label(self.root2,text="New Password",
                                  font=("times new roman",15,"bold"),bg="white",fg="black")
               new_password.place(x=50,y=220)

               self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"),show="*")
               self.txt_newpass.place(x=50,y=250,width=250)

               btn=Button(self.root2,text="Reset",
                          font=("times new roman",15,"bold"),
                          fg="white",bg="green",
                          command=self.reset_pass)
               btn.place(x=135,y=300)


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        # ========== variables =========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()


        # ============== bg image ============

        img_path = os.path.join(os.path.dirname(__file__), "college_images", "employee_img2.jpg")
        img = Image.open(img_path)
        img = img.resize((1550,800),Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        # ============= left image ============
        img_path_left = os.path.join(os.path.dirname(__file__), "college_images", "nature.jpg")
        img_left = Image.open(img_path_left)
        img_left = img.resize((1550,800),Image.LANCZOS)
        self.bg_left = ImageTk.PhotoImage(img_left)

        lbl_bg_left=Label(self.root,image=self.bg_left)
        lbl_bg_left.place(x=50,y=100,width=470,height=550)

        # ======= Main frame =============

        frame =Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl = Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # ============ label and entry =========

        # =========== row 1==================

        fname = Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)

        # =========== row 2==================

        contact = Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=200,width=250)

        email = Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)


        # ================== row 3 ==============

        security_Q = Label(frame,text="Select Security Question" , font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        security_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        security_entry.place(x=370,y=270,width=250)


        # ========== row 4 - password ================

        password= Label(frame,text="Password", font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=310)

        self.password_entry = ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=340,width=250)

        confirm_password=Label(frame,text="Confirm Password", font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=370,y=310)

        self.confirm_password_entry=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15))
        self.confirm_password_entry.place(x=370,y=340,width=250)

        # =========== checkbutton =============
        self.var_checkbox = IntVar()
        checkbtn = Checkbutton(frame,text="I Agree the terms & conditions", font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #  ============= buttons =======
        img_path4 = os.path.join(os.path.dirname(__file__), "college_images", "register-now-button1.jpg")
        img4 = Image.open(img_path4)
        img4 = img4.resize((200, 55), Image.LANCZOS)

        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(frame, image=self.photoimg4,command=self.register_data,borderwidth=0, cursor="hand2", font=("times new roman",15,"bold"))
        b1.place(x=10, y=420, width=200)

        img_path5 = os.path.join(os.path.dirname(__file__), "college_images", "loginpng.png")
        img5 = Image.open(img_path5)
        img5 = img5.resize((200, 45), Image.LANCZOS)

        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(frame, image=self.photoimg5,borderwidth=0,command=self.return_login, cursor="hand2", font=("times new roman",15,"bold"))
        b2.place(x=330, y=420, width=200)


        # ========== function declaration ===========


        def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_password.get() != self.var_confirm_password.get():
                messagebox.showerror("Error","password & confirm password must be same")
            elif self.var_checkbox.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions")
            else:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Bunty@123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","user already exists,please try another email")
                else:
                    my_cursor.execute("insert into register values(&s,&s,&s,&s,&s,&s,&s)",(
                                    self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_contact.get(),
                                    self.var_email.get(),
                                    self.var_securityQ.get(),
                                    self.var_securityA.get(),
                                    self.var_password.get()
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")


        def return_login(self):
           self.root.destroy()


if __name__ == "__main__":
    main()