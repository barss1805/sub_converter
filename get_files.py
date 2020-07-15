import glob, os, easygui

# call the window for selecting a folder with files
# вызываем окно выбора папки с файлами
input_file = easygui.diropenbox()
# print(input_file)

# os.chdir(input_file)


# for file in glob.glob("*.srt"):
#     print(file)
#     print()
# получаем пути ко всем файлам в папке
for root, dirs, files in os.walk(input_file):
    for name in files:
        # if name.endswith(".srt"):
        print(os.path.join(root, name))
