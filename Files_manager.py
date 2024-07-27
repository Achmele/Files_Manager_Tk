#____________________________________________________
#-----------------Files_Managers version 1-2 using tkinter-----------------------
import os
import os.path 
import shutil  
from win10toast import ToastNotifier
import tkinter
import time
from tkinter import ttk
import threading
from functools import partial
from tkinter import filedialog,messagebox
def try_creation_dir(dir):
    try:
        os.mkdir(dir)
    except:
        pass
notification=ToastNotifier()
def notif(a,b,c=3):
    try:notification.show_toast(title=a,msg=b,duration=c)
    except:pass
def is_myself(file):
        
        return file in myself
def increase(n):
    return n+1
img=("png","jpeg","ico","jpg")
video=("mp4","ts")
sound=("mp3","m4a")
doc=("txt","docx","pdf")
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

def Off():
    screem.quit()
    exit()


def Go(frequency=0,running=True):
    frequency=int(frequency)
    running=[True,]
    while running[0]:
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
            but.config(text="Stop",command=lambda:kill(running))
            
            if number:
                        threading.Thread(target=notif,args=("Files Manager",str(number)+" Files has been Managed By Files_manager  !!!",5)).start()
                        number=0
                    #print("fin------------")
            if check_var.get():
                pass
            else:
                running[0]=False
            time.sleep(frequency)
            print(running)
    
def set_frequence():
    if check_var.get():
        check_label.config(text="Put frequency:")
        check_label.place(x=5,y=240)
        put.place(x=150,y=240)
    else:
        check_label.config(text="")
        put.place(x=1000,y=1000)
def kill(running):
    running[0]=False
    #print(running)
    put.place(x=1000,y=1000)
    but.place(x=390,y=100)
    
    but.config(text="Select target",command=select)
    return running
def Run():
    #but.config(command=lambda:kill())
    if check_var.get():
        threading.Thread(target=notif,args=("Files Managers","Set frequency:"+str(put.get()))).start()
        a=threading.Thread(target=Go,args=(put.get()))
        a.start()
        
        pressbar=ttk.Progressbar(length=400,mode=['indeterminate'])
        
        
        pressbar.start()
        pressbar.place(x=30,y=400)
        #Go(int(put.get()))
        #time.sleep(int(put.get()))
    else:
        Go()
def select():
    #time.sleep(1)
    target=filedialog.askdirectory()
    but.place(x=390,y=351)
    but.config(text="Go !!",command=Run)
    check=tkinter.Checkbutton(text="Run frequenctlly",variable=check_var,command=set_frequence)
    check.place(x=5,y=150)
    check_label.place(x=140,y=150)
    os.chdir(target)
    #Go()
    
font1=("Bold",15)
font2=("arial",12)
red="darkred"
white="white"
green="green"
black="black"
screem=tkinter.Tk()
screem.title("Files_Manager")
style = ttk.Style()
style.theme_use("vista") 
screem.geometry("500x450")
#screem.resizable(width=False,height=False)
label1=tkinter.Label(text="File manager Launching....",fg=red,font=font1,bg=black)
label2=tkinter.Label(text="Please select the Folder how'll be Files Manager Target:",fg=red,font=font2,bg=black)
but=tkinter.Button(text="Select Target",command=select,bg=white,fg=black,font=font2)
label1.place(x=120,y=5)
label2.place(x=5,y=50)
but.place(x=390,y=100)
screem.config(bg=black)
check_var=tkinter.IntVar()
check_label=tkinter.Label(text="",bg=black,fg=green)
put=tkinter.Entry()
threading.Thread(target=notif,args=( "Files Manager","Files Manager has been launched successfully !!",6)).start()

screem.mainloop()

