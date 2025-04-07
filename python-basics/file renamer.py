import os

def rename_files(new_name):
    path = os.path.dirname(os.path.abspath(__file__))
    # files = os.listdir(path)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    folders = [fd for fd in os.listdir(path) if os.path.isdir(os.path.join(path, fd))]
    
    print(f"These are the files: ")
    for index, file in enumerate(files, start=1):
        print(index, file)
    try:
        file_index = int(input("Enter the name file number you want to change: "))
        old_file = files[file_index-1]
    except (IndexError, ValueError):
        print("Bruh pick a valid number next time")
        return
    
    old_path = os.path.join(path, old_file)
    extension = os.path.splitext(old_file)[1]
    new_file = f"{new_name}{extension}"
    new_path = os.path.join(path, new_file)

    try:
        os.rename(old_path, new_path)
        print(f"Renamed '{old_file}' → '{new_file}'")
    except Exception as e: 
        print(f"Couldn't rename it: {e}")

    print(files[file_index-1])
        
if __name__ == "__main__":
    name = input("Enter the new name of the file: ")
    rename_files(name)
