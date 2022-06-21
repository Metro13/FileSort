import os
import shutil

# Setting file type extensions dictionary

audio = {".mp3", ".m4a"}
video = {".mp4", ".mkv", ".webm", ".avi"}
documents = {".docx", ".pdf", ".xls", ".txt"}
zip_files = {".zip", ".iso", ".rar"}
apps = {".exe", ".msi"}
studio_files = {".flp", ".wav", ".mid"}
images = {".png", ".jpeg", "jpg"}
design_files = {".psd", ".xd", ".ai", ".rp"}
programming_files = {".php", ".js", ".cs"}


# Functions that split the file name and extension

def Is_Audio(files):
    return os.path.splitext(files)[1] in audio


def Is_apps(files):
    return os.path.splitext(files)[1] in apps


def Is_Video(files):
    return os.path.splitext(files)[1] in video


def Is_Document(files):
    return os.path.splitext(files)[1] in documents


def Is_ZipFiles(files):
    return os.path.splitext(files)[1] in zip_files


def Is_StudiosFiles(files):
    return os.path.splitext(files)[1] in studio_files


def Is_Images(files):
    return os.path.splitext(files)[1] in images


def Is_DesignFiles(files):
    return os.path.splitext(files)[1] in design_files


def Is_ProgrammingFiles(files):
    return os.path.splitext(files)[1] in programming_files


def Is_TrashFiles(files):
    return os.path.splitext(files)


# Code that changes the working directory to the directory that has the files that needs organizing 
os.chdir("G:/backup")

# Code that iterates into that directory and sort the files based on the extension

for file in os.listdir():
    if Is_Audio(file):
        shutil.move(file, "G:/SortedFiles/songs")
    elif Is_Images(file):
        shutil.move(file, "G:/SortedFiles/images")
    elif Is_Video(file):
        shutil.move(file, "G:/SortedFiles/Videos")
    elif Is_Document(file):
        shutil.move(file, "G:/SortedFiles/Documents")
    elif Is_DesignFiles(file):
        shutil.move(file, "G:/SortedFiles/design files")
    elif Is_ZipFiles(file):
        shutil.move(file, "G:/SortedFiles/Zip files")
    elif Is_apps(file):
        shutil.move(file, "G:/SortedFiles/Applications")
    elif Is_StudiosFiles(file):
        shutil.move(file, "G:/SortedFiles/Studio")
    elif Is_ProgrammingFiles(file):
        shutil.move(file, "G:/SortedFiles/programmingFiles")
    else:
        shutil.move(Is_TrashFiles(file), "G:/SortedFiles/Trash")
        
    
