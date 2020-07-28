# open file for read
import write_file
from googletrans import Translator


def read_file(data, name):
    translator = Translator()
    i = 2
    name = name[:-9] + "ru_RU.srt"
    with open(data, 'r') as f:
        for line in f:
            if i != 4:
                write_file.create_and_write_file(name, line)
                i += 1
            elif i == 4:
                out_text = translator.translate(line, src='en', dest='ru').text + "\n"
                write_file.create_and_write_file(name, out_text)
                i = 1
    exit()
