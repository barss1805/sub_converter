import os
import io
import re

import easygui
import conf as config
from progress.bar import IncrementalBar

from datetime import datetime
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


def counter_line(file):
    len_for_progress = 0
    with open(file) as f:
        len_for_progress = sum(1 for _ in f)
    return len_for_progress


def counter_files(select_dirs):
    count_files = 0
    for root, dirs, files in os.walk(select_dirs):
        for name in files:
            if name.endswith(f".{config.input_lang}.{config.subtitle_extention}"):
                count_files +=1
    return count_files

def run():
    input_file = easygui.diropenbox()
    total_bar = IncrementalBar('TOTAL PROGRESS', max = counter_files(input_file))
    for root, dirs, files in os.walk(input_file):
        for name in files:
            if name.endswith(f".{config.input_lang}.{config.subtitle_extention}"):
                write_name = create_name(name)
                if not os.path.isfile(os.path.join(root, write_name)):
                    with io.open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore') as rf:
                        with io.open(os.path.join(root, write_name), 'a', encoding='utf-8') as wf:
                            print(f"\nStart writing:\n {os.path.join(root, write_name)}")
                            bar = IncrementalBar('Progress curet file', max = counter_line(os.path.join(root, name)))
                            for line in rf:
                                wf.write(handler_line(line))
                                bar.next()
                        bar.finish()
                else:
                    print(f"\nfile - {write_name} - already exists!" + "\n\n")
                total_bar.next()
    total_bar.finish()

                
                

def main():
    start = datetime.now()
    print("*" * 50)
    run()
    print("*" * 50)
    print("Program running time - " + str(datetime.now() - start))


if __name__ == '__main__':
    main()
