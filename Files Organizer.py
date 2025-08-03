import os
import shutil

def clean_folder(path):
    os.chdir(path)
    nameFiles = os.listdir(path)

    listExtn = []
    for name in nameFiles:
        if os.path.isfile(name):
            extn = name.split('.')[-1]
            if extn not in listExtn:
                listExtn.append(extn)

    # Make folders
    for extn in listExtn:
        if not os.path.exists(extn):
            os.mkdir(extn)

    # Move the files the folder
    for file in nameFiles:
        if os.path.isfile(file):
            extn = file.split('.')[-1]
            shutil.move(file, os.path.join(path, extn, file))

    # Rename inside each folder
    for extn in listExtn:
        folder_path = os.path.join(path, extn)
        files = os.listdir(folder_path)
        for index, file in enumerate(files, start=1):
            old_file = os.path.join(folder_path, file)
            new_file = os.path.join(folder_path, f"({index}).{extn}")
            os.rename(old_file, new_file)
            print(f"Renamed {file} → ({index}).{extn}")

if __name__ == "__main__":
    clean_folder("D:\\Yashneel\\Game Dev\\Python\\Python Projects\\My own\\Sample junk")