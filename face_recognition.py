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
        self.stop_camera=False

        title_lbl = Label(
            self.root,
            text="Face Recognition",
            font=("times new roman", 35, "bold"),
            bg="red",
            fg="white"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top_path = os.path.join(os.path.dirname(__file__), "college_images", "u.jpg")
        img_top = Image.open(img_top_path)
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=0, y=55, width=650, height=700)

        img_bottom_path = os.path.join(os.path.dirname(__file__), "college_images", "u.jpg")
        img_bottom = Image.open(img_bottom_path)
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.Photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl2 = Label(self.root, image=self.Photoimg_bottom)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Recognition Button
        b1_1 = Button(
            self.root,
            text="Face Recognition",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="red",
            fg="white",
            command=lambda: threading.Thread(target=self.face_recog, daemon=True).start()
        )
        b1_1.place(x=365, y=620, width=200, height=40)

        stop_btn = Button(self.root,
                  text="Stop Face Recognition",
                  command=self.stop_face_recognition,
                  font=("times new roman",12,"bold"),
                  bg="red",
                  fg="white")

        stop_btn.place(x=600, y=650, width=200, height=40)


        # ========== stop camera ===============
    def stop_face_recognition(self):
        self.stop_camera = True

        if hasattr(self, "video_cap"):
            self.video_cap.release()

        cv2.destroyAllWindows()

    # ========== Attendance Logic ==============
    def mark_attendance(self, i, r, n, d):
        # 1. Define the base attendance directory
        base_dir = os.path.join(os.path.dirname(__file__), "Attendance_Reports")
        
        # 2. Get current date for Folder and Filename
        now = datetime.now()
        month_folder = now.strftime("%Y-%m") # e.g., 2026-04
        date_string = now.strftime("%d-%m-%Y") # e.g., 23-04-2026
        
        # 3. Create path: Attendance_Reports/2026-04/
        target_dir = os.path.join(base_dir, month_folder)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir) # Creates both base_dir and target_dir if they don't exist

        # 4. Final CSV path
        file_path = os.path.join(target_dir, f"{date_string}.csv")

        # 5. Initialize file with headers if it's new for the day
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as f:
                f.write("ID,Roll,Name,Department,Time,Date,Status\n")

        # 6. Writing Logic
        with open(file_path, "r+", newline="") as f:
            myDataList = f.readlines()
            id_list = [line.split(",")[0] for line in myDataList if line.strip()]

            # Prevent duplicate marking in the same lecture file
            if str(i) not in id_list:
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{i},{r},{n},{d},{dtString},{date_string},Present\n")
                f.flush()

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
        self.stop_camera = False
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, conn):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    # 1. Buffered=True is the 'Medicine' for the Unread Result error
                    my_cursor = conn.cursor(buffered=True)
                    
                    # 2. Fetch everything in ONE trip to the database
                    # Make sure these column names (Name, Roll, Dep) match your DB exactly!
                    query = "SELECT Name, Roll, Dep, Student_id FROM Student WHERE id=%s"
                    my_cursor.execute(query, (id,))
                    row = my_cursor.fetchone()

                    if row:
                        n, r, d, i = row
                    else:
                        n, r, d, i = "Unknown", "Unknown", "Unknown", "Unknown"

                    if confidence > 77:
                        cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Dept:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    
                    my_cursor.close() # Always close the cursor to keep the connection clear

                except Exception as e:
                    print(f"DB Error: {e}")


            return img # Ensure we return the modified image



        # --- SETUP ---
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(os.path.join(os.path.dirname(__file__), "classifier.xml"))

        conn = mysql.connector.connect(host="localhost", username="root", password="Bunty@123", database='face_recognizer')
        
        # FIX: Added cv2.CAP_DSHOW for better Windows compatibility
        self.video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            if self.stop_camera:
                break
            ret, img = self.video_cap.read()
            
            # CRITICAL CHECK: If frame is empty, skip this loop iteration
            if not ret or img is None:
                continue
            
            # Directly call draw_boundary to get the image back
            img = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf, conn)
            
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13: # Enter key to stop
                break
        if hasattr(self, "video_cap"):
            self.video_cap.release()
        conn.close()
        cv2.destroyAllWindows()

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