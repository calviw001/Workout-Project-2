from pathlib import Path
import math


def read_and_create_text_list(file_name, key, a_list, branch):
    message_length = 0
    encrypted_message = ""
    current_directory = Path.cwd()
    file_path = current_directory / file_name
    f = open(file_path, "r")
    for line in f:
        encrypted_message += line
        message_length += len(line)
    f.close()
    row_length = message_length / key
    row_length = math.ceil(row_length)
    for character in encrypted_message:
        branch += character
        if len(branch) == row_length:
            a_list.append(branch)
            branch = ""
    a_list.append(branch)
    print(a_list)
