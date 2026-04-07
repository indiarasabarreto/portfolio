import os
import shutil
import time


base_directory = os.path.dirname(os.path.abspath(__file__))

base_path = os.path.join(base_directory, 'organized_files')


while True:
    print("Checking files...")

    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)

    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                destination = os.path.join(base_directory, 'files')
                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, filename))
                print(f'Movido: {filename} to {destination}')
    
    time.sleep(60)
    



    