import os

import easygui

import read_file

# call the window for selecting a folder with files
# вызываем окно выбора папки с файлами
input_file = easygui.diropenbox()

# get the paths to all files in the folder
# получаем пути ко всем файлам в папке
for root, dirs, files in os.walk(input_file):
    for name in files:
        if name.endswith(".srt"):
            pas_for_write = os.path.join(root) + "\\"
            print(os.path.join(root, name))
            full_path = os.path.join(root, name)
            read_file.read_file(full_path, pas_for_write, name)
