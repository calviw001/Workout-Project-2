import sys
from pathlib import Path
import encrypt_message
import key_validation

def check_input_file(file_name):
  current_directory = Path.cwd()
  file_path = current_directory / file_name
  if file_path.exists() and file_path.is_file():
    return file_path.stat().st_size
  else:
    print("Your input file does not exist!!")
    sys.exit()


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
  test_key = '11'
  file_size = check_input_file(input_file)
  e_d = input().strip()
  # print(file_size)
  if key_validation.check_test_key(test_key, file_size):
    if e_d == '-e':
      text_list = encrypt_message.read_and_create_text_list(input_file, int(test_key), [], "")
      print(text_list)
      encrypted_message = encrypt_message.encrypt_text(text_list)
      print(encrypted_message)
      write_into_file(encrypted_message, output_file)
  else:
    print("You entered an invlaid secret key!")
  

main()
