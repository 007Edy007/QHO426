def display_chars(file_path, no_of_characters):
    with open(file_path) as file:
        data = file.read(no_of_charachters)
        print(data)
def run():
    display_chars(file_path:"library.txt",no_of_characters:10)

    