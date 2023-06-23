import os

def list_files():
    files_and_folders = os.listdir()
    for item in files_and_folders:
        if os.path.isfile(item):
            print(item)

def list_files():
    files_and_folders = os.listdir()
    files = [item for item in files_and_folders if os.path.isfile(item)]
    for item in files:
        print(item)

def save_directory_contents():
    files_and_folders = os.listdir()
    files = []
    dirs = []

    for item in files_and_folders:
        files.append(item) if os.path.isfile(item) else dirs.append(item)

    file_path = os.path.join(os.getcwd(), "listdir.txt")

    with open(file_path, "w") as f:
        f.write("files: " + ", ".join(files) + "\n")
        f.write("dirs: " + ", ".join(dirs) + "\n")

    print(f"Содержимое рабочей директории сохранено в файле '{file_path}'.")
