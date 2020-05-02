"""
Helper-: Internet/Code With Harry
Author-: @@
Python Project
"""
import os
from shutil import move
from datetime import datetime 
def Folder(Folder_Name):
    if not os.path.exists(Folder_Name):
        os.mkdir(Folder_Name)
def moving(file, folder):
    global No_Of_File_Moved
    move(file, folder)
    No_Of_File_Moved = No_Of_File_Moved + 1
    with open("MovingLog", "a") as f:
        Datetime = datetime.now().strftime("%d-%m-%Y at %H:%M:%S")
        file = file.split("/")[-1]
        f.write(f"Date {Datetime} You Moved {file}\n")
        f.write("----------------------------------------------------------------")
extension = { 
"audio" : ['.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl','.m3u'],
"text" : ['.txt','.doc','.docx','.odt','.pdf','.rtf','.tex','.wks','.wps','.wpd'],
"video" : ['.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'],
"images" : ['.ai','.bmp','.gif','.jpg','.jpeg','.png','.ps','.psd','.svg','.tif','.tiff','.cr2'],
"internet" : ['.asp','.aspx','.cer','.cfm','.cgi','.pl','.css','.htm','.js','.jsp','.part','.php','.rss','.xhtml','.html'],
"compressed" : ['.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip'],
"disc" : ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
"database" : ['.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.xml','.json'],
"executables" : ['.apk','.bat','.com','.exe','.gadget','.jar','.wsf'],
"fonts" : ['.fnt','.fon','.otf','.ttf'],
"presentations" : ['.key','.odp','.pps','.ppt','.pptx'],
"c" : ['.c', '.h'],
"java" : ['.class', '.java'],
"python" : ['.py'],
"shell" : ['.sh'],
"spreadsheets" : ['.ods','.xlr','.xls','.xlsx'],
"system" : ['.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ico','.ini','.lnk','.msi','.sys','.tmp']}
Format = list(extension.keys())
Main = ["audio", "text", "video", "images"]
No_Of_File_Moved = 0
for i in Main:
    Format.remove(i)
files = os.listdir()
files.remove("main.py")
for i in files:
    path = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(path, i)
    i = "." + i.split('.')[-1]
    if i in extension["audio"]:
        Folder("Audio")
        moving(file, path+"/Audio")
    elif i in extension["text"]:
        Folder("Text")
        moving(file, path+"/Text")
    elif i in extension["video"]:
        Folder("Video")
        moving(file, path+"/Video")
    elif i in extension["images"]:
        Folder("Images")
        moving(file, path+"/Images")
    else:
        for o in Format:
            if i in extension[o]:
                Folder("Other")
                try:
                    os.mkdir(f"Other/{o}/")
                except:
                    print("", end="")
                moving(file, f"{path}/Other/{o}")
print("Number Of Files Moved-: " + str(No_Of_File_Moved))
if No_Of_File_Moved != 0:
    print("Log File Saved To Your Current WOrking Directory\n")
