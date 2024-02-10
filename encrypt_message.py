from pathlib import Path


def read_and_create_text_list(file_name, key, a_list, branch):
  current_directory = Path.cwd()
  file_path = current_directory / file_name
  f = open(file_path, "r")
  for text_message in f:
    for character in text_message:
      branch += character
      # print(branch)
      if len(branch) == key:
        a_list.append(branch)
        branch = ""
    a_list.append(branch)
  f.close()
  return a_list


def encrypt_text(text_list):
    matrix = []
    for character in text_list[0]:
        matrix.append(character)
    for text_section in text_list[1:]:
        i = 0
        for character in text_section:
            matrix[i] += character
            i += 1
    print(matrix)
    encrypted_message = ""
    for row in matrix:
        encrypted_message += row

    return encrypted_message