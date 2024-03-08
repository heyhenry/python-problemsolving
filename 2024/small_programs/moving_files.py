import shutil
import os

src_file = r"C:\Users\Henry Han\Desktop\Daily Maplestory.xlsx"
dst_directory = r"C:\Users\Henry Han\Desktop\test_directory"

path = r"C:\Users\Henry Han\Desktop"
desktop_content = os.listdir(path)
directories = []
# directories = [d for d in desktop_content if os.path.isdir(d)]

for i in desktop_content:
    # if os.path.isdir(os.path.join(path,i)):
    if os.path.isdir(path+f'\{i}'):
        directories.append(i)

print(directories)

