# Collecting all the modules needed
import os, zipfile
from tkinter import Tk, filedialog

class LockFiles:
    def __init__(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
    def __getFiles(self):
        "This is private method"
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
    def __getArchives(self):
        "This is private method"
        return filedialog.askopenfilenames(title="Choose Archive", filetypes=[
            ("RAR", "*.rar"),
            ("ZIP", "*.zip")
        ])
    def abs_compile2rar(self):
        # Compile to Archive with absolute path
        """
        Inside Archive
            /path/filename.extension
        """
        fileslist = self.__getFiles()
        with zipfile.ZipFile("member.rar", "w") as zipper:
            for file in fileslist:
                zipper.write(file)
    def rel_compile2rar(self):
        # Compile to Archive with relative path
        """
        Inside Archive
            Member/filename.extension
        """
        fileslist = self.__getFiles()
        with zipfile.ZipFile("member.rar", "w") as zipper:
            for file in fileslist:
                zipper.write(file, os.path.join("Member", os.path.basename(file)))
    def deflateArchive(self):
        archives = self.__getArchives()
        for archive in archives:
            with zipfile.ZipFile(archive, 'r') as zipfile_:
                # print(zipfile_.namelist()) List all the files inside the archive
                filepath, _ = os.path.splitext(archive)
                zipfile_.extractall(filepath)

compiler = LockFiles()

# Compiling
compiler.abs_compile2rar()
compiler.rel_compile2rar()
compiler.deflateArchive()