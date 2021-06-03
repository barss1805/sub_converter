import os
import io
from posixpath import join
import re

import easygui
import conf as config
from progress.bar import IncrementalBar

from deep_translator import GoogleTranslator


def create_name(name):
    input_lang = config.input_lang
    change_lang = config.change_lang
    output_name = re.sub(input_lang, change_lang, name)
    return output_name


def translated_line(line):
    try:
        out_text = GoogleTranslator(source='auto', target=config.target_to_translate).translate(line) + "\n"
        return out_text
    except TypeError as e:
        print(e)
        return line

def handler_line(line):
    not_translated = ['^\d*$','^\d*:\d*:\d*', ' ^\s*$']
    for x in not_translated:
        if re.search(x, line):
            return line
    return translated_line(line)


def counter_line_in_file(file):
    len_for_progress = 0
    with open(file) as f:
        len_for_progress = sum(1 for _ in f)
    return len_for_progress


def read_write(read_file):
    write_name = create_name(read_file)
    if not os.path.isfile(write_name):
        with io.open(read_file, 'r', encoding='utf-8', errors='ignore') as rf:
            with io.open(write_name, 'a', encoding='utf-8') as wf:
                print(f"\nStart writing:\n {write_name}")
                bar = IncrementalBar('Progress curet file', max = counter_line_in_file(read_file))
                for line in rf:
                    bar.next()
                    wf.write(handler_line(line))
                print(f"\nEnd writing:\n {write_name}")
    else:
        print(f"\nfile - {write_name} - already exists!" + "\n\n")
                          


def main():
    input_file = easygui.diropenbox()
    for root, dirs, files in os.walk(input_file):
        for name in files:
            if name.endswith(f".{config.input_lang}.{config.subtitle_extention}"):
                read_write(join(root,name)) 


if __name__ == '__main__':
    main()
