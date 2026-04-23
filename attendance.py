from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_attendance_id=StringVar()
        self.var_attendance_roll=StringVar()
        self.var_attendance_name=StringVar()
        self.var_attendance_dep=StringVar()
        self.var_attendance_time=StringVar()
        self.var_attendance_date=StringVar()
        self.var_attendance_atten=StringVar()

        # first image
        img_path = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img = Image.open(img_path)
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # second image
        img_path1 = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img1 = Image.open(img_path1)
        img1 = img1.resize((800, 200), Image.LANCZOS)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=800, height=200)

        # bg image
        img_path3 = os.path.join(os.path.dirname(__file__), "college_images", "bg.jpg")
        img3 = Image.open(img_path3)
        img3 = img3.resize((1530, 710), Image.LANCZOS)

        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold")
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main Frame
        main_frame= Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance")
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img4 = Image.open(img_left)
        img4 = img4.resize((720, 130), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl4 = Label(Left_frame, image=self.photoimg4)
        f_lbl4.place(x=5, y=0, width=720, height=130)

        # left inside frame

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=300)

        # label and entry 
        # attendance_id
        attendance_id_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendance_id_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendance_id, font=("times new roman", 13, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=4, pady=8)

        roll_label_entry = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attendance_roll, font=("comicsansns 11 bold", 13, "bold"))
        roll_label_entry.grid(row=0, column=3,pady=8)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        name_label.grid(row=1, column=0)

        name_label_entry = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attendance_name, font=("comicsansns 11 bold", 13, "bold"))
        name_label_entry.grid(row=1, column=1,pady=8)

        # department
        dep_Label = Label(left_inside_frame, text="Department:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        dep_Label.grid(row=1, column=2)

        dep_label_entry = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attendance_dep, font=("comicsansns 11 bold", 13, "bold"))
        dep_label_entry.grid(row=1, column=3,pady=8)


        # Time
        time_Label = Label(left_inside_frame, text="Time:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        time_Label.grid(row=2, column=0)

        time_label_entry = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attendance_time, font=("comicsansns 11 bold", 13, "bold"))
        time_label_entry.grid(row=2, column=1,pady=8)


        # Date
        date_Label = Label(left_inside_frame, text="Date:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        date_Label.grid(row=2, column=2)

        date_label_entry = ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attendance_date, font=("comicsansns 11 bold", 13, "bold"))
        date_label_entry.grid(row=2, column=3,pady=8)  


        # Attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("comicsansns 11 bold", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0)

        self.attendance_status = ttk.Combobox(
            left_inside_frame,
            font=("comicsansns 11 bold", 13, "bold"),
            state="readonly",textvariable=self.var_attendance_atten,
            width=20,
        )
        self.attendance_status["values"] = ("Status", "Present", "Absent")
        self.attendance_status.grid(row=3, column=1,pady=8)
        self.attendance_status.current(0)

        # Buttons frame
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=400,width=715,height=35)

        import_btn = Button(btn_frame, text="Import CSV", width=17, command=self.importCSV,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", width=17, command=self.exportCSV, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        # right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details")
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)


        # Scroll bar table

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # fetch data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*.csv"),("All File","*.*")],parent=self.root)
        if fln:
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)


    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*.csv"),("All File","*.*")],parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attendance_id.set(rows[0])
        self.var_attendance_roll.set(rows[1])
        self.var_attendance_name.set(rows[2])
        self.var_attendance_dep.set(rows[3])
        self.var_attendance_time.set(rows[4])
        self.var_attendance_date.set(rows[5])
        self.var_attendance_atten.set(rows[6])


    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_attendance_roll.set("")
        self.var_attendance_name.set("")
        self.var_attendance_dep.set("")
        self.var_attendance_time.set("")
        self.var_attendance_date.set("")
        self.var_attendance_atten.set("")








if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()

