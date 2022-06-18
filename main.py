import os
import shutil

audio = {".mp3", ".m4a"}
video = {".mp4", ".mkv", ".webm", ".avi"}
documents = {".docx", ".pdf", ".xls", ".txt"}
zip_files = {".zip", ".iso", ".rar"}
apps = {".exe", ".msi"}
studio_files = {".flp", ".wav", ".mid"}
images = {".png", ".jpeg", "jpg"}
design_files = {".psd", ".xd", ".ai", ".rp"}
trash_files = {".php", ".js", ".cs"}


def Is_Audio(files):
    return os.path.splitext(file)[1] in audio


def Is_apps(files):
    return os.path.splitext(file)[1] in apps


def Is_Video(files):
    return os.path.splitext(file)[1] in video


def Is_Document(files):
    return os.path.splitext(file)[1] in documents


def Is_ZipFiles(files):
    return os.path.splitext(file)[1] in zip_files


def Is_StudiosFiles(files):
    return os.path.splitext(file)[1] in studio_files


def Is_Images(files):
    return os.path.splitext(file)[1] in images


def Is_DesignFiles(files):
    return os.path.splitext(file)[1] in design_files


def Is_TrashFiles(files):
    return os.path.splitext(file)[1] in trash_files


os.chdir("G:/backup")

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
    elif Is_TrashFiles(file):
        shutil.move(file, "G:/SortedFiles/Trash")
    elif Is_StudiosFiles(file):
        shutil.move(file, "G:/SortedFiles/Studio")
