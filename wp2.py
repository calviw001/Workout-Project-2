import sys
from pathlib import Path
import encrypt_message


def check_input_file(file_name):
  current_directory = Path.cwd()
  file_path = current_directory / file_name
  if file_path.exists() and file_path.is_file():
    return file_path.stat().st_size
  else:
    print("Your input file does not exist!!")
    sys.exit()


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


def write_into_file(encrypted_message, file_name):
  current_directory = Path.cwd()
  file_path = current_directory / file_name
  f = open(file_path, "w")
  f.write(encrypted_message)
  f.close()


def main():
  input_file = "originaltext.txt"
  output_file = "encryptedtext.txt"
  # test_string1 = "This.is.the.UCI.ICS32.Programming.with.Software.Libraries.course!"
  test_key = 11
  file_size = check_input_file(input_file)
  print(file_size)
  text_list = read_and_create_text_list(input_file, test_key, [], "")
  encrypted_message = encrypt_message.encrypt(text_list)
  print(encrypted_message)
  write_into_file(encrypted_message, output_file)
  

main()
