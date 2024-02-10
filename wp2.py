import sys
from pathlib import Path
import encrypt_message
import decrpyt_message
import key_validation


def get_user_inputs():
    try:
        assert len(sys.argv) == 5
        e_d = sys.argv[1]
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        key = sys.argv[4]
        return e_d, input_file, output_file, key
    except AssertionError:
        print("Encryption Usage: python wp2.py -e input_file_name output_file_name key")
        print("Decryption Usage: python wp2.py -d input_file_name output_file_name key")
        sys.exit()


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
  e_d, input_file, output_file, key = get_user_inputs()
  # python wp2.py -e originaltext.txt encryptedtext.txt 11
  # python wp2.py -d encryptedtext.txt decryptedtext.txt 11
  file_size = check_input_file(input_file)
  if key_validation.check_test_key(key, file_size):
    if e_d == '-e':
      text_list_E = encrypt_message.read_and_create_text_list_E(input_file, int(key), [], "")
      # print(text_list_E)
      encrypted_message = encrypt_message.encrypt_text(text_list_E)
      # print(encrypted_message)
      write_into_file(encrypted_message, output_file)
    if e_d == '-d':
      text_list_D = decrpyt_message.read_and_create_text_list_D(input_file, int(key), [], "")
      # print(text_list_D)
      decrypted_message = decrpyt_message.decrypt_text(text_list_D)
      # print(decrypted_message)
      write_into_file(decrypted_message, output_file)
  

main()
