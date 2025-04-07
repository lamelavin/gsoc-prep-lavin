import os
import shutil
from colorama import init, Fore

init(autoreset=True)

FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.doc', '.txt'],
    'videos': ['.mp4', '.mkv', '.mov'],
    'music': ['.mp3', '.wav'],
    'code': ['.py', '.js', '.java', '.cpp'],
    'archives': ['.zip', '.rar', '.7z'],
}

def get_folder(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder
    return 'others'

def file_sorter():
    path = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(path)

    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path) or file == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(file)
        ext = ext.lower()

        folder_name = get_folder(ext)
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        try:
            shutil.move(full_path, os.path.join(folder_path, file))
            print(Fore.GREEN + f"[+] Moved: {file} → {folder_name}/")
        except Exception as e:
            print(Fore.RED + f"[X] Failed to move {file}: {e}")

if __name__ == "__main__":
    file_sorter()
