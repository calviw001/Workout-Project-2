def encrypt(text_list):
    matrix = []
    for character in text_list[0]:
        matrix.append(character)
        #print(rows_list)

    for text_section in text_list[1:]:
        i = 0
        for character in text_section:
            matrix[i] += character
            i += 1
    #print(rows_list)

    encrypted_message = ""
    for row in matrix:
        encrypted_message += row

    return encrypted_message