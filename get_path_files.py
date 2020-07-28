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
            # print(os.path.join(root, name))
            _path = os.path.join(root, name)
            print(name)
            read_file.read_file(_path, name)
