from PIL import Image as PILImage
from tkinter import Tk, Label, Button, filedialog, Scale, messagebox, Entry
import tkinter as tk
import sys

sys.setrecursionlimit(3000)

class DPIChanger():
    def __init__(self, winTitle, xSize, ySize, *args):
        self.window = tk.Tk()
        if args:
            self.window.configure(bg=args)
        self.window.geometry(f'{xSize}x{ySize}')
        self.window.title(winTitle)
        self.window.iconbitmap("ImageDPI.ico")
        self.chooseImageButton = Button(text="Choose Image", bd=3, command=self.chooseImageFunc)
        self.chooseImageButton.place(x=23, y=20)
        self.chooseSaveTo = Button(text="Choose where to save to", bd=3, command=self.chooseSaveFunc)
        self.chooseSaveTo.place(x=150, y=20)
        self.dpiScale = Scale(from_=5000, to=0)
        self.dpiScale.place(x=0, y=70)
        self.dpiScaleTwo = Scale(from_=5000, to=0)
        self.dpiScaleTwo.place(x=40, y=70)
        self.newImageName = Label(text="Enter new image name", font=("Courier", 12))
        self.newImageName.place(x=110, y=70)
        self.newImageEntry = Entry(bd=3)
        self.newImageEntry.place(x=110, y=100)
        self.changeDPIBtn = Button(text="Submit", bd=3, command=self.changeDPI)
        self.changeDPIBtn.place(x=110, y=145)
        self.window.mainloop()

    def chooseImageFunc(self):
        self.getImage = filedialog.askopenfilename()
        messagebox.showinfo("Image ", self.getImage)
        self.getImageExtension = self.getImage.rsplit(".", 1)
        self.imageExtension = self.getImageExtension[1]

    def chooseSaveFunc(self):
        self.savedFolder = filedialog.askdirectory()
        messagebox.showinfo("Folder", self.savedFolder)

    def changeDPI(self):
        self.scaleNum = self.dpiScale.get()
        self.scaleNumTwo = self.dpiScaleTwo.get()
        self.theNewImage = PILImage.open(self.getImage)
        self.theNewImage.save(self.savedFolder + "/" + self.newImageEntry.get() + "." + self.imageExtension , dpi=(self.scaleNum, self.scaleNumTwo))
        messagebox.showinfo("Saved", self.savedFolder + "/" + self.newImageEntry.get() + "." + self.imageExtension)
    
DPIGUI = DPIChanger("Change DPI", 350, 200)
