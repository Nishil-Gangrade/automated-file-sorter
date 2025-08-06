import os
import shutil

path = r"C:/Users/Nishil Gangrade/Documents/Proj_DummyData/"
file_names = os.listdir(path)
print(file_names)
folder_names = ['img files', 'text files']
for folder in folder_names:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
for file in file_names:
    full_file_path = os.path.join(path, file)
    
    if os.path.isfile(full_file_path): 
        if file.endswith('.txt'):
            shutil.move(full_file_path, os.path.join(path, 'text files', file))
        elif file.endswith('.png'):
            shutil.move(full_file_path, os.path.join(path, 'img files', file))
