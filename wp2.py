import sys
from pathlib import Path
import encrypt_message
import decrpyt_message
import key_validation

def check_input_file(file_name):
  current_directory = Path.cwd()
  file_path = current_directory / file_name
  if file_path.exists() and file_path.is_file():
    return file_path.stat().st_size
  else:
    print("Your input file does not exist!!")
    sys.exit()


def write_into_file(message, file_name):
  current_directory = Path.cwd()
  file_path = current_directory / file_name
  f = open(file_path, "w")
  f.write(message)
  f.close()


def main():
  input_file = "originaltext.txt"
  output_file = "encryptedtext.txt"
  output_file2 = "decryptedtext.txt"
  test_key = '4'
  file_size = check_input_file(input_file)
  e_d = '-d'
  # print(file_size)
  if key_validation.check_test_key(test_key, file_size):
    if e_d == '-e':
      text_list_E = encrypt_message.read_and_create_text_list_E(input_file, int(test_key), [], "")
      # print(text_list_E)
      encrypted_message = encrypt_message.encrypt_text(text_list_E)
      # print(encrypted_message)
      # print(len(encrypted_message))
      write_into_file(encrypted_message, output_file)
    if e_d == '-d':
      text_list_D = decrpyt_message.read_and_create_text_list_D(output_file, int(test_key), [], "")
      # print(text_list_D)
      decrypted_message = decrpyt_message.decrypt_text(text_list_D)
      # print(decrypted_message)
      # print(len(decrypted_message))
      write_into_file(decrypted_message, output_file2)
  else:
    print("You entered an invlaid secret key!")
  

main()
