from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

# code formatted

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl = Label(self.root, text="Train data set", font=("times new roman", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top img - using os.path.join for reliability
        img_top_path = os.path.join(os.path.dirname(__file__), "college_images", "u.jpg")
        img_top = Image.open(img_top_path)
        img_top = img_top.resize((1530, 325), Image.LANCZOS)

        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl2 = Label(self.root, image=self.photoimg_top)
        f_lbl2.place(x=0, y=55, width=1530, height=325)

        # Button
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier,
                      font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # bottom img
        img_bottom_path = os.path.join(os.path.dirname(__file__), "college_images", "u.jpg")
        img_bottom = Image.open(img_bottom_path)
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)

        self.Photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = Label(self.root, image=self.Photoimg_bottom)
        f_lbl2.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        # FIX: Define the absolute path to the data directory
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        
        # Check if directory exists and has files
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data folder not found at: {data_dir}", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            # Skip non-image files like .DS_Store or system files
            if not image.endswith(('.jpg', '.png', '.jpeg')):
                continue
                
            img = Image.open(image).convert('L')  # Gray Scale image
            imageNp = np.array(img, 'uint8')
            
            # Extracting ID from filename: "user.ID.count.jpg"
            try:
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
            except Exception:
                # Skips files that don't follow the naming convention
                continue

        ids = np.array(ids)

        # Train the classifier and save
        if len(faces) == 0:
            messagebox.showerror("Error", "No datasets found to train!", parent=self.root)
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        
        # FIX: Save the classifier in the current project directory
        clf_path = os.path.join(os.path.dirname(__file__), "classifier.xml")
        clf.write(clf_path)
        
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed and saved to classifier.xml")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()