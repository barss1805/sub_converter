
def create_and_write_file(name_file, information_for_recording):
    with open("hello.txt", "a") as file:
        file.write(information_for_recording)