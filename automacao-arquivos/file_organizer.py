import os
import shutil

file_organizer = 'files'
destination_folder = 'organized_files'

extensions = {
    'images': ['.WebP', '.png'],
    'documents': ['.pdf'],
    'spreadsheets': ['.xlsx']
}

for filename in os.listdir(file_organizer):
    file_path = os.path.join(file_organizer, filename)

    for paste, types in extensions.items():
        if any(filename.endswith(ext) for ext in types):
            destination_path = os.path.join(destination_folder, paste)
            os.makedirs(destination_path, exist_ok=True)
            shutil.move(file_path, os.path.join(destination_path, filename))
            break