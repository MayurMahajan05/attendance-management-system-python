from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Developer:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(
            self.root,
            text="DEVELOPER",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=0, y=0, width=1530, height=70)

        img_path = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img_top = Image.open(img_path)
        img_top = img_top.resize((1530, 720), Image.LANCZOS)

        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img1 = Image.open(img_top1)
        img1 = img1.resize((200, 200), Image.LANCZOS)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(main_frame, image=self.photoimg1)
        f_lbl1.place(x=300, y=0, width=200, height=200)

        # Developer Info
        dev_lbl = Label(
            main_frame,
            text="Hello, My name is ABC",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="blue"
        )
        dev_lbl.place(x=0, y=5)

        dev_lbl1 = Label(
            main_frame,
            text="I'm Full Stack Developer",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="blue"
        )
        dev_lbl1.place(x=0, y=40)

        img_top2 = os.path.join(os.path.dirname(__file__), "college_images", "Stanford.jpg")
        img2 = Image.open(img_top2)
        img2 = img2.resize((500, 390), Image.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(main_frame, image=self.photoimg2)
        f_lbl2.place(x=0, y=210, width=500, height=390)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()