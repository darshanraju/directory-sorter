import os
import sys
from pathlib import Path
import shutil

try:
    dir = sys.argv[1]
except IndexError:
    dir = "/Users/darshan.raju/watch-dog-scripts/testing-dir/"
    dir = str(Path().absolute())

file_types = [".pdf", ".jpeg", ".png", ".gif", ".doc", ".mp3", ".zip"]

files = os.listdir(dir)
for file_name in files:
    for file_type in file_types:
        if file_name.endswith(file_type):
            print(file_name, " ends in: " + file_type)
            file_dest = os.path.join(dir,file_type.strip("."))
            print(file_dest)
            if os.path.isdir(file_dest) == False:
                print("Path doesnt exist")
                os.mkdir(file_dest)
            shutil.move(os.path.join(dir,file_name),file_dest)

