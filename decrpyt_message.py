from pathlib import Path



def read_and_create_text_list(file_name, key, a_list, branch):
    encrypted_message = ""
    current_directory = Path.cwd()
    file_path = current_directory / file_name
    f = open(file_path, "r")
    for line in f:
        encrypted_message += line
    print(encrypted_message)