from tkinter import *
import os
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from tkinter import messagebox
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime

# main.py formatted

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        # Stanford img
        img_path = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img = Image.open(img_path)
        img = img.resize((500, 130), Image.LANCZOS)

        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second img
        img_path1 = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img1 = Image.open(img_path1)
        img1 = img1.resize((500, 130), Image.LANCZOS)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # third img
        img_path2 = os.path.join(os.path.dirname(__file__), "college_images", "u.jpg")
        img2 = Image.open(img_path2)
        img2 = img2.resize((500, 130), Image.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        # bg image
        img_path3 = os.path.join(os.path.dirname(__file__), "college_images", "bg.jpg")
        img3 = Image.open(img_path3)
        img3 = img3.resize((1530, 710), Image.LANCZOS)

        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold")
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # ============== Time =================

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

        # ---------------- ROW 1 ---------------- #

        # Student button
        img_path4 = os.path.join(os.path.dirname(__file__), "college_images", "chat_people.jpg")
        img4 = Image.open(img_path4)
        img4 = img4.resize((220, 220), Image.LANCZOS)

        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(  
            bg_img,
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            font=("times new roman", 15, "bold"),bg="darkblue",
            fg="white"
        )
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect Face button
        img_path5 = os.path.join(os.path.dirname(__file__), "college_images", "face_detector1.jpg")
        img5 = Image.open(img_path5)
        img5 = img5.resize((220, 220), Image.LANCZOS)

        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Face Detecter",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            command=self.face_data,
            bg="darkblue",
            fg="white"
        )
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance button
        img_path6 = os.path.join(os.path.dirname(__file__), "college_images", "report.jpg")
        img6 = Image.open(img_path6)
        img6 = img6.resize((220, 220), Image.LANCZOS)

        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Attendance",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
            command=self.attendance_data
        )
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help button
        img_path7 = os.path.join(os.path.dirname(__file__), "college_images", "help_desk.jpg")
        img7 = Image.open(img_path7)
        img7 = img7.resize((220, 220), Image.LANCZOS)

        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2" , command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Help Desk",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white" , command=self.help_data
        )
        b1_1.place(x=1100, y=300, width=220, height=40)

        # ---------------- ROW 2 ---------------- #

        # Train button
        img_path8 = os.path.join(os.path.dirname(__file__), "college_images", "Train.jpg")
        img8 = Image.open(img_path8)
        img8 = img8.resize((220, 220), Image.LANCZOS)

        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Train Data",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
            command=self.train_data
        )
        b1_1.place(x=200, y=580, width=220, height=40)

        # Photos
        img_path9 = os.path.join(os.path.dirname(__file__), "college_images", "crowd.jpg")
        img9 = Image.open(img_path9)
        img9 = img9.resize((220, 220), Image.LANCZOS)

        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Photos",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
            command=self.open_img
        )
        b1_1.place(x=500, y=580, width=220, height=40)

        # Developer
        img_path10 = os.path.join(os.path.dirname(__file__), "college_images", "mgmt.jpg")
        img10 = Image.open(img_path10)
        img10 = img10.resize((220, 220), Image.LANCZOS)

        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10,command=self.developer_data, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Developer",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            command=self.developer_data,
            fg="white"
        )
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit face button
        img_path11 = os.path.join(os.path.dirname(__file__), "college_images", "exit.jpg")
        img11 = Image.open(img_path11)
        img11 = img11.resize((220, 220), Image.LANCZOS)

        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
            command=self.iExit
        )
        b1_1.place(x=1100, y=580, width=220, height=40)

    # =========== Functions buttons =================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def open_img(self):
        data_path = os.path.join(os.path.dirname(__file__), "data")

        if os.path.exists(data_path):
            os.startfile(data_path)
        else:
            messagebox.showerror("Error", "Data folder not found!", parent=self.root)

    def iExit(self):
        result = messagebox.askyesno(
            "Face Recognition",
            "Are you sure you want to exit?",
            parent=self.root
        )

        if result:
            self.root.destroy()

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
