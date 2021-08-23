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
with zipfile.ZipFile("Archivename", "Mode", "Compression Mode") as zipper:
    zipper.write("Filepath[Filename]", "Arcname")
````
**Archivename:** (Required)
    The name of archive that will be created with supported extension <br>
    Example: archive.rar

**Mode:** (Required)
    *w*
        Write Mode
            Create new file with the name provided, if already exist then rewrite the file entirely
            (Used to Create new archive)
    *r*
        Read Mode
            Read the file with the name provided
            (Used to extract archive)

**Compression Mode:** (Optional)
    Read Documentation for further information

**Filepath or Filename:** (Required)
    Full path of file or filename (If exist in same location as the location of execution of script) that is to be added to the archive
    Path maybe Relative or Absolute

**Arcname:** (Optional)
    Basename or Absolute file path
    Sometime, when we want to add file from different location to the archive like
        fileone: /path/location/fileone.txt and
        filetwo: /path/location-2/filetwo.txt
        then the files will he added as
        location/fileone.txt and 
        location-2/filetwo.txt

        to avoid such situtation, write method of ZipFile supports arcname.
        This basically remove the provided path from filepath