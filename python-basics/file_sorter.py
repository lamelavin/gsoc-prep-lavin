import os
import shutil

def file_sorter(directory):
  
  if not os.isdir(directory):
    choice = input(f"Directory {directory} doesn't exist. Do you want to create one? (y/n): ")
    if choice == 'y':
      os.mkdir(directory)
    elif choice == 'n':
      return
    else:
      print(f"Invalid input '{choice}'.")

  for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
      extension = file_name.split('.')[-1] if '.' in file_name else 'no_extension'
      folder_extension = os.path.join(directory, extension)
      if not os.path.isdir(folder_extension):
        os.mkdir(folder_extension)
  shutil.move(file_path, os.path.join(directory, file_name))
  print("File organization finish")
