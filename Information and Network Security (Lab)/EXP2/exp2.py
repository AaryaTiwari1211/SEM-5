def printArray(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()


def textGen(arr, n):
    text = ""
    for i in range(n):
        for j in range(n):
            # print(arr[i][j], end=" ")
            text += arr[i][j]
    return text


def row_transpose_encrypt(text, key):
    text_length = len(text)
    print("Length of the text: ", text_length)

    key1 = key.split(" ")

    for i in range(text_length):
        if i*i >= text_length:
            size = i
            break
    row = size
    col = size
    twoD = [[" " for i in range(col)] for j in range(row)]
    index = 0
    for i in range(row):
        for j in range(col):
            if index < text_length:
                twoD[i][j] = text[index]
                index += 1
            else:
                twoD[i][j] = '_'

    printArray(twoD, row)
    print()
    twoD_2 = twoD.copy()

    for i in range(len(key1)):  # [3,1,2]
        twoD_2[i] = twoD[int(key1[i])-1]

    printArray(twoD_2, row)
    cipher_text = textGen(twoD_2, row)
    print("Cipher Text: ", cipher_text)
    return cipher_text


def row_transpose_decrypt(text, key):
    text_length = len(text)
    print("Length of the text: ", text_length)

    key1 = key.split(" ")

    for i in range(text_length):
        if i*i >= text_length:
            size = i
            break
    row = size
    col = size
    twoD = [[" " for i in range(col)] for j in range(row)]
    index = 0
    for i in range(row):
        for j in range(col):
            if index < text_length:
                twoD[i][j] = text[index]
                index += 1
            else:
                twoD[i][j] = '_'
    printArray(twoD, row)
    print()
    twoD_2 = twoD.copy()

    for i in range(len(key1)):
        twoD_2[int(key1[i])-1] = twoD[i]

    printArray(twoD_2, row)

    plain_text = textGen(twoD_2, row)
    print("Plain Text: ", plain_text)
    return plain_text


def column_transpose_encrypt(text, key):
    text_length = len(text)
    print("Length of the text: ", text_length)

    key1 = key.split(" ")

    for i in range(text_length):
        if i*i >= text_length:
            size = i
            break
    row = size
    col = size

    twoD = [[" " for i in range(col)] for j in range(row)]
    index = 0
    for i in range(row):
        for j in range(col):
            if index < text_length:
                twoD[i][j] = text[index]
                index += 1
            else:
                twoD[i][j] = '_'
    printArray(twoD, col)
    print()
    key1 = [int(i)-1 for i in key1]
    transposed_array = []
    for row in twoD:
        transposed_row = []
        for i in key1:
            transposed_row.append(row[i])
        transposed_array.append(transposed_row)

    printArray(transposed_array, col)
    cipher_text = textGen(transposed_array, col)
    print("Cipher Text: ", cipher_text)
    return cipher_text


def column_transpose_decrypt(text, key):
    text_length = len(text)
    key1 = key.split(" ")

    for i in range(text_length):
        if i * i >= text_length:
            size = i
            break
    row = size
    col = size

    twoD = [[" " for i in range(col)] for j in range(row)]
    index = 0
    for i in range(row):
        for j in range(col):
            if index < text_length:
                twoD[i][j] = text[index]
                index += 1
            else:
                twoD[i][j] = '_'
    printArray(twoD, col)
    print()
    key1 = [int(i) - 1 for i in key1]
    original_array = [[" " for i in range(col)] for j in range(row)] 
    for i in range(row):
        for j in range(col):
            original_array[i][key1[j]] = twoD[i][j]
    printArray(original_array, col)

    plain_text = ""
    for i in range(row):
        for j in range(col):
            plain_text += original_array[i][j]
    print("Plain Text: ", plain_text)
    return plain_text



def double_transposition_encrypt(text, key1, key2):
    intermediate_cipher = row_transpose_encrypt(text, key1)
    final_cipher = column_transpose_encrypt(intermediate_cipher, key2)
    return final_cipher


def double_transposition_decrypt(cipher_text, key1, key2):
    intermediate_plain = column_transpose_decrypt(cipher_text, key2)
    original_plain = row_transpose_decrypt(intermediate_plain, key1)
    return original_plain


x = True
while x:
    print("Enter 1 for Row Transpose Encryption")
    print("Enter 2 for Row Transpose Decryption")
    print("Enter 3 for Column Transpose Encryption")
    print("Enter 4 for Column Transpose Decryption")
    print("Enter 5 for Double Transposition Encryption")
    print("Enter 6 for Double Transposition Decryption")
    print("Enter 7 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_text = input("Enter the text: ")
        user_key = input("Enter the key: ")
        cipher_text = row_transpose_encrypt(user_text, user_key)
    elif choice == 2:
        user_text = input("Enter the text: ")
        user_key = input("Enter the key: ")
        plain_text = row_transpose_decrypt(user_text, user_key)
    elif choice == 3:
        user_text = input("Enter the text: ")
        user_key = input("Enter the key: ")
        cipher_text = column_transpose_encrypt(user_text, user_key)
    elif choice == 4:
        user_text = input("Enter the text: ")
        user_key = input("Enter the key: ")
        plain_text = column_transpose_decrypt(user_text, user_key)
    elif choice == 5:
        user_text = input("Enter the text: ")
        user_key1 = input("Enter the key1: ")
        user_key2 = input("Enter the key2: ")
        cipher_text = double_transposition_encrypt(user_text, user_key1, user_key2)
    elif choice == 6:
        user_text = input("Enter the text: ")
        user_key1 = input("Enter the key1: ")
        user_key2 = input("Enter the key2: ")
        plain_text = double_transposition_decrypt(user_text, user_key1, user_key2)
    elif choice == 7:
        x = False
    else:
        print("Invalid Choice. Please choose a correct input!!")
