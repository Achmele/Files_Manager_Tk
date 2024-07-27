from win10toast import ToastNotifier
import os
import os.path
import tkinter
import shutil
import time
from tkinter import filedialog
def try_creation_dir(dir):
    try:
        os.mkdir(dir)
    except:
        pass
        
def is_myself(file):
        
        return file in myself
def increase(n):
    return n+1
img=("png","jpeg","ico","jpg")
video=("mp4","ts")
sound=("mp3","m4a")
doc=("txt","docx")
compress=("zip","rar")
exe=("exe","py","c","c++","bat","vbs")
dirs=("Images","Video","Sounds","Documents","Others","Programms","Compressed")
ext_dir={
    img:dirs[0],
    video:dirs[1],
    sound:dirs[2],
    doc:dirs[3],
    exe:dirs[5],
    compress:dirs[6],
}
myself=("Files_manager.py","Files_manager.bat")
notification=ToastNotifier()
target=filedialog.askdirectory()
       
   

notification.show_toast(title="Files Manager",msg="Files Manager has been launched successfully !!",duration=3)
os.chdir(target)
while True:
    try:
            files=os.listdir()
            number=0
            for file in files:
                    #print("je suis la")
                    ext=file.split(".")
                    ext=ext[-1]
                    if ext in img :
                        try_creation_dir(ext_dir[img])
                        shutil.move(file,"Images/"+file)
                        number=increase(number)
                    elif ext in video:
                        try_creation_dir(ext_dir[video])
                        shutil.move(file,"Video/"+file)
                        number=increase(number)
                    elif ext in sound :
                        try_creation_dir(ext_dir[sound])
                        shutil.move(file,"Sounds/"+file)
                        number=increase(number)
                    elif ext in doc :
                        try_creation_dir(ext_dir[doc])
                        shutil.move(file,"Documents/"+file)
                        number=increase(number)
                    elif ext in exe and not is_myself(file) :
                        try_creation_dir(ext_dir[exe])
                        shutil.move(file,"Programms/"+file)
                        number=increase(number)
                    elif ext in compress :
                        try_creation_dir(ext_dir[compress])
                        shutil.move(file,"Compressed/"+file)
                        number=increase(number)
                    else :
                        if  is_myself(file) or os.path.isdir(file):
                            pass
                        else:
                            try_creation_dir(dirs[4])
                            shutil.move(file,"Others/"+file)
                            number=increase(number)
                #but.config(text="Stop",command=screem.quit)
            if number:
                    notification.show_toast("Files Manager",str(number)+" Files has been Managed By Files_manager  !!!",duration=5)
                    number=0
            time.sleep(3)
            
    except:pass