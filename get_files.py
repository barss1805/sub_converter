import glob, os, easygui

# call the window for selecting a folder with files
# вызываем окно выбора папки с файлами
input_file = easygui.diropenbox()
print(input_file)

# os.chdir(input_file)


# for file in glob.glob("*.srt"):
#     print(file)
#     print()
for root, dirs, files in os.walk("D:\lessons\pyt_n\\11 Web Scraping with Python"):
    print("ggggggggggggg")
    for file in files:
        if file.endswith(".srt"):
             print(os.path.join(root, file))