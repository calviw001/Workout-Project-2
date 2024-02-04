def read_text(line, key, a_list, branch):
  for character in line:
    branch += character
    # print(branch)
    if len(branch) == key:
      a_list.append(branch)
      branch = ""
  a_list.append(branch)
  return a_list


def create_cypher(text_list):
  rows_list = []
  for character in text_list[0]:
    rows_list.append(character)
  #print(rows_list)

  for text_section in text_list[1:]:
    i = 0
    for character in text_section:
      rows_list[i] += character
      i += 1
  #print(rows_list)

  return rows_list

  
def main():
  test_string1 = "This.is.the.UCI.ICS32.Programming.with.Software.Libraries.course!"
  test_key = 11
  text_list = read_text(test_string1, test_key, [], "")
  print(text_list)
  encrypted_text_rows = create_cypher(text_list)
  print(encrypted_text_rows)
  

main()
