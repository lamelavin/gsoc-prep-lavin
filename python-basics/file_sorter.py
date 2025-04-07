import os
import shutil 
from colorama import Fore, init

init(autoreset=True)

FILE_TYPE = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.doc', '.txt'],
    'videos': ['.mp4', '.mkv', '.mov'],
    'music': ['.mp3', '.wav'],
    'code': ['.py', '.js', '.java', '.cpp'],
    'archives': ['.zip', '.rar', '.7z'],
}

def get_folder(extension):
    for folder, extensions in FILE_TYPE.items():
        if extension in extensions:
            return folder
    return 'others'

def file_sorter():
    path = os.path.dirname(os.path.abspath(__file__))
    # print(path)
    files = os.listdir(path)

    for file in files:
        # print(file)
        full_path = os.path.join(path, file)
        # print(full_path)
        
        # print(os.path.basename(__file__))
        # print(os.path.isdir(full_path))
        if os.path.isdir(full_path) or file == os.path.basename(__file__):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()

        folder_name = get_folder(extension)
        folder_path = os.path.join(path, extension)

        os.makedirs(extension, exist_ok=True)

        try:
            shutil.move(full_path, os.path.join(folder_path, file))
            print(Fore.GREEN + f"[+] Moved: {file} => {folder_name}")
        except Exception as e:
            print(Fore.RED + f"[X] Failed to move {file}: {e}")


if __name__ == "__main__":
    file_sorter()
