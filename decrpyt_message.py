from pathlib import Path
import math


def read_and_create_text_list_D(file_name, key, a_list, branch):
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
    # print(row_length)
    total_positions = key * row_length
    # print(total_positions)
    # print(message_length)
    num_unfilled_pos = total_positions - message_length
    i = 0
    fill_pos = True
    for character in encrypted_message:
        branch += character
        if key - i == num_unfilled_pos:
            fill_pos = False
            if len(branch) + 1 == row_length:
                a_list.append(branch)
                # print(f"{i}: {branch}")
                branch = ""
        elif fill_pos and len(branch) == row_length:
            a_list.append(branch)
            i += 1
            branch = ""
    a_list.append(branch)
    return a_list


def decrypt_text(text_list):
    branch = ""
    matrix = []
    for i in range(len(text_list[0])):
        for text_section in text_list:
            try:
                branch += text_section[i]
            except IndexError:
                pass
        matrix.append(branch)
        branch = ""
    # print(matrix)
    decrypted_message = ""
    for row in matrix:
        decrypted_message += row

    return decrypted_message