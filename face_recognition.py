from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import threading

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # stop camera variable
        self.session_id = datetime.now().strftime("%H-%M-%S")
        self.stop_camera=False
        self.var_start_roll = StringVar()
        self.var_end_roll = StringVar()
        self.var_teacher = StringVar()
        self.var_Lab_subject = StringVar()
        self.var_duration = StringVar()
        self.var_year = StringVar()
        self.var_dept = StringVar()
        self.var_div = StringVar()
        self.var_batch = StringVar()

        # --- GLOBAL UI CONSTANTS ---
        LIST_DEPARTMENTS = ["Select Department", "Computer", "IT", "Civil", "Civil & Infra", "Chemical", "Humanities", "AI & DS", "Mechanical", "Electronics"]
        LIST_COURSES = ["Select Course", "FE", "SE", "TE", "BE"]
        LIST_YEARS = ["Select Year", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]
        LIST_Lab_SUBJECTS = ["Select Lab","Blockchain Lab" , "Cloud Computing Lab"]
        LIST_SEMESTERS = ["Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6", "Sem-7", "Sem-8"]
        LIST_DIVISIONS = ["Select Division", "A", "B", "C"]
        LIST_BATCHES = ["Select Batch", "B1", "B2", "B3", "B4"]  # Added based on your previous requirement

# Title
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Left Image (Camera Area Placeholder)
        img_top_path = os.path.join(os.path.dirname(__file__), "college_images", "u.jpg")
        img_top = Image.open(img_top_path)
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimg_top, bd=2, relief=RIDGE)
        f_lbl1.place(x=10, y=55, width=650, height=700)

        # Right Side - Session Details Frame
        details_frame = LabelFrame(self.root, bd=2, bg="white", relief=RIDGE, text="Session Configuration", font=("times new roman", 12, "bold"))
        details_frame.place(x=670, y=55, width=840, height=350)

                # Start Roll No
        lbl_start = Label(details_frame, text="Start Roll:", font=("times new roman", 11, "bold"), bg="white")
        lbl_start.grid(row=4, column=0, padx=10, pady=15, sticky=W)
        entry_start = ttk.Entry(details_frame, textvariable=self.var_start_roll, width=20)
        entry_start.grid(row=4, column=1, padx=10, pady=15)

        # End Roll No
        lbl_end = Label(details_frame, text="End Roll:", font=("times new roman", 11, "bold"), bg="white")
        lbl_end.grid(row=4, column=2, padx=10, pady=15, sticky=W)
        entry_end = ttk.Entry(details_frame, textvariable=self.var_end_roll, width=20)
        entry_end.grid(row=4, column=3, padx=10, pady=15)

        # --- Row 0: Teacher & Subject ---
        lbl_teacher = Label(details_frame, text="Teacher Name:", font=("times new roman", 11, "bold"), bg="white")
        lbl_teacher.grid(row=0, column=0, padx=10, pady=15, sticky=W)
        entry_teacher = ttk.Entry(details_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 11))
        entry_teacher.grid(row=0, column=1, padx=10, pady=15)

        lbl_sub = Label(details_frame, text="Lab Subject:", font=("times new roman", 11, "bold"), bg="white")
        lbl_sub.grid(row=0, column=2, padx=10, pady=15, sticky=W)
        combo_sub = ttk.Combobox(details_frame, textvariable=self.var_Lab_subject, values=LIST_Lab_SUBJECTS, font=("times new roman", 11), state="readonly", width=18)
        combo_sub.current(0)
        combo_sub.grid(row=0, column=3, padx=10, pady=15)

        # --- Row 1: Dept & Year ---
        lbl_dept = Label(details_frame, text="Department:", font=("times new roman", 11, "bold"), bg="white")
        lbl_dept.grid(row=1, column=0, padx=10, pady=15, sticky=W)
        combo_dept = ttk.Combobox(details_frame, textvariable=self.var_dept, values=LIST_DEPARTMENTS, font=("times new roman", 11), state="readonly", width=18)
        combo_dept.current(0)
        combo_dept.grid(row=1, column=1, padx=10, pady=15)

        lbl_year = Label(details_frame, text="Year (Course):", font=("times new roman", 11, "bold"), bg="white")
        lbl_year.grid(row=1, column=2, padx=10, pady=15, sticky=W)
        combo_year = ttk.Combobox(details_frame, textvariable=self.var_year, values=LIST_COURSES, font=("times new roman", 11), state="readonly", width=18)
        combo_year.current(0)
        combo_year.grid(row=1, column=3, padx=10, pady=15)

        # --- Row 2: Div & Batch ---
        lbl_div = Label(details_frame, text="Division:", font=("times new roman", 11, "bold"), bg="white")
        lbl_div.grid(row=2, column=0, padx=10, pady=15, sticky=W)
        combo_div = ttk.Combobox(details_frame, textvariable=self.var_div, values=LIST_DIVISIONS, font=("times new roman", 11), state="readonly", width=18)
        combo_div.current(0)
        combo_div.grid(row=2, column=1, padx=10, pady=15)

        lbl_batch = Label(details_frame, text="Batch:", font=("times new roman", 11, "bold"), bg="white")
        lbl_batch.grid(row=2, column=2, padx=10, pady=15, sticky=W)
        combo_batch = ttk.Combobox(details_frame, textvariable=self.var_batch, values=LIST_BATCHES, font=("times new roman", 11), state="readonly", width=18)
        combo_batch.current(0)
        combo_batch.grid(row=2, column=3, padx=10, pady=15)

        # --- Row 3: Duration ---
        lbl_dur = Label(details_frame, text="Duration (Mins):", font=("times new roman", 11, "bold"), bg="white")
        lbl_dur.grid(row=3, column=0, padx=10, pady=15, sticky=W)
        entry_dur = ttk.Entry(details_frame, textvariable=self.var_duration, width=20, font=("times new roman", 11))
        entry_dur.grid(row=3, column=1, padx=10, pady=15)

        # Control Buttons
        btn_frame = Frame(details_frame, bd=2, bg="white")
        btn_frame.place(x=10, y=260, width=800, height=60)

        start_btn = Button(btn_frame, text="Start Recognition", command=lambda: threading.Thread(target=self.face_recog, daemon=True).start(), font=("times new roman", 13, "bold"), bg="blue", fg="white", width=25)
        start_btn.grid(row=0, column=0, padx=10)

        stop_btn = Button(btn_frame, text="Force Stop", command=self.stop_face_recognition, font=("times new roman", 13, "bold"), bg="darkred", fg="white", width=25)
        stop_btn.grid(row=0, column=1, padx=10)


        # ========== stop camera ===============
    def stop_face_recognition(self):
        self.stop_camera = True

        if hasattr(self, "video_cap"):
            self.video_cap.release()

        cv2.destroyAllWindows()

    # ========== Attendance Logic ==============


    def mark_attendance(self, i, r, n, d):
        # 1. Get the directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        reports_dir = os.path.join(current_dir, "Attendance_Reports")
        
        # 2. Folder logic (Month-wise)
        now = datetime.now()
        month_folder = now.strftime("%Y-%m")
        target_path = os.path.join(reports_dir, month_folder)
        
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        # 3. UNIQUE FILENAME LOGIC
        # We use a 'session_time' variable so the filename is locked 
        # to the moment the teacher started the camera.
        sub_name = self.var_Lab_subject.get().replace(" ", "_")
        batch_name = self.var_batch.get()
        date_str = now.strftime("%d-%m-%Y")
        
        # This uses the specific time the recognition started (stored in self.session_id)
        filename = f"{sub_name}_{batch_name}_{date_str}_{self.session_id}.csv"
        file_full_path = os.path.join(target_path, filename)

        # 4. Write Data
        new_file = not os.path.exists(file_full_path)
        with open(file_full_path, "a", newline="") as f:
            if new_file:
                f.write(f"SESSION REPORT\n")
                f.write(f"Teacher: {self.var_teacher.get()}, Subject: {self.var_Lab_subject.get()}, Batch: {batch_name}\n")
                f.write(f"Session Started: {date_str} {self.session_id}\n")
                f.write("-" * 50 + "\n")
                f.write("ID,Roll,Name,Department,Time,Status\n")

            # Duplicate check for THIS specific session file
            with open(file_full_path, "r") as check_f:
                if str(i) not in [line.split(",")[0] for line in check_f.readlines()]:
                    t_string = now.strftime("%H:%M:%S")
                    f.write(f"{i},{r},{n},{d},{t_string},Present\n")


    # def mark_attendance(self, i, r, n, d):
    #     # 1. Define the base attendance directory
    #     base_dir = os.path.join(os.path.dirname(__file__), "Attendance_Reports")
        
    #     # 2. Get current date for Folder and Filename
    #     now = datetime.now()
    #     month_folder = now.strftime("%Y-%m") # e.g., 2026-04
    #     date_string = now.strftime("%d-%m-%Y") # e.g., 23-04-2026
        
    #     # 3. Create path: Attendance_Reports/2026-04/
    #     target_dir = os.path.join(base_dir, month_folder)
    #     if not os.path.exists(target_dir):
    #         os.makedirs(target_dir) # Creates both base_dir and target_dir if they don't exist

    #     # 4. Final CSV path
    #     file_path = os.path.join(target_dir, f"{date_string}.csv")

    #     # 5. Initialize file with headers if it's new for the day
    #     if not os.path.exists(file_path):
    #         with open(file_path, "w", newline="") as f:
    #             f.write("ID,Roll,Name,Department,Time,Date,Status\n")

    #     # 6. Writing Logic
    #     with open(file_path, "r+", newline="") as f:
    #         myDataList = f.readlines()
    #         id_list = [line.split(",")[0] for line in myDataList if line.strip()]

    #         # Prevent duplicate marking in the same lecture file
    #         if str(i) not in id_list:
    #             dtString = now.strftime("%H:%M:%S")
    #             f.write(f"{i},{r},{n},{d},{dtString},{date_string},Present\n")
    #             f.flush()



    # def mark_attendance(self, i, r, n, d):
    #     # This gets the directory where face_recognition.py is located
    #     current_dir = os.path.dirname(__file__) 
    #     # This joins that directory with your filename
    #     file_path = os.path.join(current_dir, "kiran.csv")

    #     if not os.path.exists(file_path):
    #         with open(file_path, "w", newline="\n") as f:
    #             f.writelines("ID,Roll,Name,Department,Time,Date,Status")

    #     with open(file_path, "r+", newline="\n") as f:
    #         myDataList = f.readlines()
    #         name_list = []
    #         for line in myDataList:
    #             entry = line.split(",")
    #             name_list.append(entry[0]) # Checking ID to prevent duplicates

    #         if str(i) not in name_list:
    #             now = datetime.now()
    #             d1 = now.strftime("%d/%m/%Y")
    #             dtString = now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # ============ Face Recognition Main Logic ===========

    def face_recog(self):
        # Validation before starting
        if self.var_teacher.get() == "" or self.var_Lab_subject.get() == "Select Subject":
            messagebox.showerror("Error", "Please fill Session Details first", parent=self.root)
            return

        self.stop_camera = False
        start_timestamp = datetime.now()
        
        try:
            limit_seconds = int(self.var_duration.get()) * 60
        except:
            limit_seconds = 3600 # Default 1 hour

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf, conn):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    my_cursor = conn.cursor(buffered=True)
                    # Fetching Division to compare with UI constant
                    query = "SELECT Name, Roll, Dep, Student_id, Division FROM Student WHERE id=%s"
                    my_cursor.execute(query, (id,))
                    row = my_cursor.fetchone()

                    if row and confidence > 77:
                        n, r, d, i, stud_div = row
                        
                        # --- RANGE & DIVISION FILTER LOGIC ---
                        try:
                            start_r = int(self.var_start_roll.get())
                            end_r = int(self.var_end_roll.get())
                            current_r = int(r)
                        except:
                            start_r, end_r, current_r = 0, 0, -1 # Fail filter if non-numeric

                        # Validate: Same Division AND Roll is within Range
                        if stud_div == self.var_div.get() and start_r <= current_r <= end_r:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3) # Green
                            cv2.putText(img, f"{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                            self.mark_attendance(i, r, n, d)
                        else:
                            # Recognized but wrong Batch/Div
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 165, 255), 3) # Orange
                            cv2.putText(img, "Wrong Batch", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 165, 255), 2)
                    
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3) # Red
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    
                    my_cursor.close()
                except Exception as e:
                    print(f"DB Error: {e}")

            return img

        # --- CAMERA EXECUTION ---
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(os.path.join(os.path.dirname(__file__), "classifier.xml"))
        conn = mysql.connector.connect(host="localhost", username="root", password="Bunty@123", database='face_recognizer')
        
        self.video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            if self.stop_camera:
                break
            
            # --- TIMER CHECK ---
            elapsed = (datetime.now() - start_timestamp).total_seconds()
            if elapsed > limit_seconds:
                print("Duration reached. Closing session.")
                break

            ret, img = self.video_cap.read()
            if not ret or img is None: continue
            
            img = draw_boundary(img, faceCascade, 1.1, 10, clf, conn)
            cv2.imshow("Lab Attendance", img)

            if cv2.waitKey(1) == 13: break

        self.video_cap.release()
        conn.close()
        cv2.destroyAllWindows()



    # def face_recog(self):
    #     self.stop_camera = False
    #     def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, conn):
    #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

    #         coord = []
    #         for (x, y, w, h) in features:
    #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    #             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
    #             confidence = int((100 * (1 - predict / 300)))

    #             try:
    #                 # 1. Buffered=True is the 'Medicine' for the Unread Result error
    #                 my_cursor = conn.cursor(buffered=True)
                    
    #                 # 2. Fetch everything in ONE trip to the database
    #                 # Make sure these column names (Name, Roll, Dep) match your DB exactly!
    #                 query = "SELECT Name, Roll, Dep, Student_id FROM Student WHERE id=%s"
    #                 my_cursor.execute(query, (id,))
    #                 row = my_cursor.fetchone()

    #                 if row:
    #                     n, r, d, i = row
    #                 else:
    #                     n, r, d, i = "Unknown", "Unknown", "Unknown", "Unknown"

    #                 if confidence > 77:
    #                     cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
    #                     cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
    #                     cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
    #                     cv2.putText(img, f"Dept:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
    #                     self.mark_attendance(i, r, n, d)
    #                 else:
    #                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    #                     cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    
    #                 my_cursor.close() # Always close the cursor to keep the connection clear

    #             except Exception as e:
    #                 print(f"DB Error: {e}")


    #         return img # Ensure we return the modified image



    #     # --- SETUP ---
    #     faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    #     clf = cv2.face.LBPHFaceRecognizer_create()
    #     clf.read(os.path.join(os.path.dirname(__file__), "classifier.xml"))

    #     conn = mysql.connector.connect(host="localhost", username="root", password="Bunty@123", database='face_recognizer')
        
    #     # FIX: Added cv2.CAP_DSHOW for better Windows compatibility
    #     self.video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    #     while True:
    #         if self.stop_camera:
    #             break
    #         ret, img = self.video_cap.read()
            
    #         # CRITICAL CHECK: If frame is empty, skip this loop iteration
    #         if not ret or img is None:
    #             continue
            
    #         # Directly call draw_boundary to get the image back
    #         img = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf, conn)
            
    #         cv2.imshow("Face Recognition", img)

    #         if cv2.waitKey(1) == 13: # Enter key to stop
    #             break
    #     if hasattr(self, "video_cap"):
    #         self.video_cap.release()
    #     conn.close()
    #     cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()



# face recog code 
                # try:
                #     my_cursor = conn.cursor()
                #     my_cursor.execute(f"select Name from Student where Student_id={id}")
                #     n = my_cursor.fetchone()
                #     n = n[0] if n else "Unknown"

                #     my_cursor.execute(f"select Roll from Student where Student_id={id}")
                #     r = my_cursor.fetchone()
                #     r = r[0] if r else "Unknown"

                #     my_cursor.execute(f"select Dep from Student where Student_id={id}")
                #     d = my_cursor.fetchone()
                #     d = d[0] if d else "Unknown"

                #     my_cursor.execute(f"select Student_id from Student where Student_id={id}")
                #     i = my_cursor.fetchone()
                #     i = i[0] if i else "Unknown"

                #     if confidence > 77:
                #         cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #         cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #         cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #         cv2.putText(img, f"Dept:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #         self.mark_attendance(i, r, n, d)
                #     else:
                #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                #         cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                # except Exception as e:
                #     print(f"DB Error: {e}")