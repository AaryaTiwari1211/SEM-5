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

    for i in range(len(key1)): # [3,1,2]
        twoD_2[i] = twoD[int(key1[i])-1] #

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
    original_array = []
    for i in range(row):
        original_row = []
        for j in range(col):
            original_row.append(twoD[i][key1[j]])
        original_array.append(original_row)
    printArray(original_array, col)

    plain_text = ""
    for row in original_array:
        for char in row:
            plain_text += char
    print("Plain Text: ", plain_text)
    return plain_text

# user_text = input("Enter the text: ")
# user_key = input("Enter the key: ")

# cipher_text = row_transpose_encrypt(user_text, user_key)
# plain_text = row_transpose_decrypt(cipher_text, user_key)

# cipher_text = column_transpose_encrypt(user_text, user_key)
# plain_text = column_transpose_decrypt(cipher_text, user_key)

# column_transpose_encrypt(user_text, user_key)

x = True
while x:
    print("Enter 1 for Row Transpose Encryption")
    print("Enter 2 for Row Transpose Decryption")
    print("Enter 3 for Column Transpose Encryption")
    print("Enter 4 for Column Transpose Decryption")
    print("Enter 5 to exit")
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
        x = False


