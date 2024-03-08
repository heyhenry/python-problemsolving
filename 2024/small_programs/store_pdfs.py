import shutil
import os

path = r"C:\Users\Henry Han\Desktop"
desktop_content = os.listdir(path)
target_directory = r"C:\Users\Henry Han\Desktop\pdfs"

files_on_desktop = []

for file in desktop_content:
    if not os.path.isdir(os.path.join(path,file)):
        files_on_desktop.append(file)

for i in files_on_desktop:
    if i[i.rfind('.'):] == '.pdf':
        shutil.move(os.path.join(path,i), target_directory)





