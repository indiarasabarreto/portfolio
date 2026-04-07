import os
import shutil


base_directory = os.path.dirname(os.path.abspath(__file__))


""" 
    source_folders = [
    os.path.join(base_directory, './organized_files/documents'),
    os.path.join(base_directory, './organized_files/spreadsheets'),
    os.path.join(base_directory, './organized_files/images')
] 


destination_folder = os.path.join(base_directory, './files')

for folder in source_folders:
    if not os.path.exists(folder):
        print(f"Source folder '{folder}' does not exist. Skipping.")
        continue

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            destination = os.path.join(destination_folder, filename)
            os.makedirs(destination_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved '{filename}' to '{destination_folder}'") """



base_path = os.path.join(base_directory, 'organized_files')

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)

    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                destination = os.path.join(base_directory, 'files')
                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, filename))
                print(f'Movido: {filename} → {destination}')