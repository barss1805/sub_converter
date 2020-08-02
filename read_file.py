# open file for read
import write_file
import os
from googletrans import Translator


def read_file(data, path_for_write_file, name):
    translator = Translator()
    i = 2
    name = name[:-9] + "ru_RU.srt"
    if os.path.isfile(path_for_write_file+name):
        print("File " + name + " exists")
    else:
        with open(data, 'r') as f:
            for line in f:
                if i != 4:
                    write_file.create_and_write_file(path_for_write_file, name, line)
                    i += 1
                elif i == 4:
                    out_text = translator.translate(line, src='en', dest='ru').text + "\n"
                    write_file.create_and_write_file(path_for_write_file, name, out_text)
                    i = 1
