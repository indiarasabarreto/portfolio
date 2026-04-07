import os
import shutil


base_directory = os.path.dirname(os.path.abspath(__file__))


file_organizer = os.path.join(base_directory, 'organized_files')
destination_folder = os.path.join(base_directory, 'files')



extensions = {
    'images': ['.WebP', '.png'],
    'documents': ['.pdf'],
    'spreadsheets': ['.xlsx']
}


if not os.path.exists(file_organizer):
    print(f'Error: The directory "{file_organizer}" does not exist.')
    exit()

for filename in os.listdir(file_organizer):
    file_path = os.path.join(file_organizer, filename)

    if os.path.isfile(file_path):
        name, extension = os.path.splitext(filename)


        for paste, types in extensions.items():
            if extension.lower() in types:
                destination = os.path.join(destination_folder, paste)
                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, filename))
                print(f'Moved: {filename} to {destination}')
                break