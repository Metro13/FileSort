# class for formatting files
import os.path
import shutil
import glob


# Iterates the backup directory and returns new object of files
def GetFilename(names):
    filename = os.path.basename(names)
    return filename


# creates files directory based on pattern and moves files in the new directory




