import os
import shutil
from datetime import datetime

# Dictionary to map file types to folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".wmv", ".flv", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".cpp", ".c", ".java", ".sh"]
}

def get_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            return folder
    return "Others"

def organize_directory(directory):
    for filename in os.listdir(directory):
        src = os.path.join(directory, filename)
        if os.path.isfile(src):
            folder = get_folder(filename)
            dest_folder = os.path.join(directory, folder)
            os.makedirs(dest_folder, exist_ok=True)
            dest = os.path.join(dest_folder, filename)

            # Handle duplicates
            base, ext = os.path.splitext(filename)
            count = 1
            while os.path.exists(dest):
                dest = os.path.join(dest_folder, f"{base}_{count}{ext}")
                count += 1
            shutil.move(src, dest)
            print(f"Moved: {filename} -> {folder}/")

if __name__ == "__main__":
    folder = input("Enter the path of the folder to organize: ").strip()
    if os.path.isdir(folder):
        organize_directory(folder)
        print("Organization complete!")
    else:
        print("Folder does not exist.")
