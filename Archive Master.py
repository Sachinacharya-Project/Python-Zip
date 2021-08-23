# Collecting all the modules needed
import os, zipfile
from tkinter import Tk, filedialog

class LockFiles:
    def __init__(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
    def getFiles(self):
        return filedialog.askopenfilenames(title='Choose Images or Videos', filetypes=[
            ("All Images", "*.jpg *.jpeg *.png *.bmp *.gif *.tif *.tiff *.eps"),
            ("JPEG", "*.jpg *.jpeg"),
            ("PNG", "*.png"),
            ("Bitmap", "*.bmp"),
            ("GIF", "*.gif"),
            ("TIFF", "*.tif *.tiff"),
            ("EPS", "*.eps"),
            ("Video", "*.mp4 *.avi *.mkv"),
            ("Show all", "*.*")
        ])
    def compile2rar(self):
        fileslist = self.getFiles()
        count = 1
        with zipfile.ZipFile("member.zip", "w") as ziper:
            for file in fileslist:
                print(count, file)
                count += 1
                ziper.write(file, os.path.join("Member", os.path.basename(file)))

LockFiles().compile2rar()