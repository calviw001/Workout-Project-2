from pathlib import Path
import encrypt_message

def read_text(file_name, key, a_list, branch):
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


def main():
  input_file = "originaltext.txt"
  # output_file = "encryptedtext.txt"
  # test_string1 = "This.is.the.UCI.ICS32.Programming.with.Software.Libraries.course!"
  test_key = 11
  text_list = read_text(input_file, test_key, [], "")
  # print(text_list)
  encrypted_message = encrypt_message.create_cypher(text_list)
  print(encrypted_message)
  

main()
