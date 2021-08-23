# Python Zip
A little python script to create and extract Archive (example *.rar and *.zip)

## Source
This program uses the python module named [zipfile](https://docs.python.org/3/library/zipfile.html) (Visit Documentation for more details)

## Used (Modules)
1. [zipfile](https://docs.python.org/3/library/zipfile.html)
2. [os](https://docs.python.org/3/library/os.html)
3. [Tkinter](https://docs.python.org/3/library/tk.html)

## Syntax
1. For creating Archive
````python
import zipfile
with zipfile.ZipFile("archivename", "mode", "compression_mode") as zipper:
    zipper.write("filepath[filename]", "arcname")
````
_Arch