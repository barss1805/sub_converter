
def create_and_write_file(name_file, information_for_recording):
    with open(name_file, "a", encoding='utf-8') as file:
        file.write(information_for_recording)