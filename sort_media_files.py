import os
from pathlib import Path
import shutil

# Change details here as necessary
USER = "jason"
TARGET_FOLDER = "All_Media"
TARGET_FOLDER_PATH = Path(f"C:\\Users\\{USER}\\Downloads\\{TARGET_FOLDER}")

# Don't touch this one
FILE_TYPES = []

def check_move_file(file: str) -> None:
    file_parts = file.split(".")
    file_name = file_parts[0]
    file_extension = file_parts[1].lower()

    # Create directory if it doesn't exist
    if file_extension not in FILE_TYPES:
        FILE_TYPES.append(file_extension)
        os.makedirs(file_extension)
    
    # Copy the files into the correct directory
    source_file = Path(f"{TARGET_FOLDER_PATH}\\{file}")
    destination_folder = Path(f"{TARGET_FOLDER_PATH}(1)\\{file_extension}")
    shutil.copy(source_file, destination_folder)
    print(f"Moving {source_file} to {destination_folder}")


def process_folder(path) -> None:
    for root, dirs, files in os.walk(path):
        for file in files:
            file_parts = check_move_file(file)


def main():
    # First create new directory to house directories for the varying file types, and change the working directory into that directory
    dir_name = Path(f"{TARGET_FOLDER_PATH}(1)")
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        os.chdir(dir_name)

    # Start searching through the folder and creating directories as necessary
    process_folder(TARGET_FOLDER_PATH)
     

if __name__ == "__main__":
    main()


