def playfair_encryption(message, key):
    alphabets = "abcdefghiklmnopqrstuvwxyz"
    n = 5
    twoD_arr = [["" for i in range(n)] for j in range(n)]
    x = 0
    message = message.lower()
    key = key.lower()
    key_set = set()

    for i in range(n):
        for j in range(n):
            if x < len(key) and key[x] not in key_set:
                twoD_arr[i][j] = key[x]
                key_set.add(key[x])
                x += 1

    y = 0
    for i in range(n):
        for j in range(n):
            if twoD_arr[i][j] == "":
                while alphabets[y] in key_set or alphabets[y] == "j":
                    y += 1
                twoD_arr[i][j] = alphabets[y]
                key_set.add(alphabets[y])
                y += 1

    # Display the 2D array
    for row in twoD_arr:
        print(row)

    message_current = message
    for i in range(len(message_current) - 1):
        if (
            message_current[i] == message_current[i + 1]
            and message_current[i] != "z"
            and message_current[i] != "x"
        ):
            message_current = message_current[: i + 1] + "z" + message_current[i + 2 :]

    encrypted = ""
    it1 = 0
    it2 = 1
    while it2 < len(message_current):
        letter1 = message_current[it1]
        letter2 = message_current[it2]
        index1, index2, index3, index4 = None, None, None, None

        # Find indices for the letters in the Playfair matrix
        for i in range(n):
            for j in range(n):
                if twoD_arr[i][j] == letter1:
                    index1, index2 = i, j
                if twoD_arr[i][j] == letter2:
                    index3, index4 = i, j

        if index2 == index4:
            encrypted += twoD_arr[(index1 + 1) % n][index2] + twoD_arr[(index3 + 1) % n][index4]

        # Case 2 - When both are in the same column
        elif index1 == index3:
            encrypted += twoD_arr[index1][(index2 + 1) % n] + twoD_arr[index3][(index4 + 1) % n]

        # Case 3 - when both are away from each other
        else:
            encrypted += twoD_arr[index1][index4] + twoD_arr[index3][index2]

        print(message_current[it1], message_current[it2])
        it1 += 2
        it2 += 2
    print(encrypted)
    return encrypted


def playfair_decryption(message, key):
    alphabets = "abcdefghiklmnopqrstuvwxyz"
    n = 5
    twoD_arr = [["" for i in range(n)] for j in range(n)]
    x = 0
    message = message.lower()
    key = key.lower()
    key_set = set()

    # Fill the 2D array with key values
    for i in range(n):
        for j in range(n):
            if x < len(key) and key[x] not in key_set:
                twoD_arr[i][j] = key[x]
                key_set.add(key[x])
                x += 1

    y = 0
    for i in range(n):
        for j in range(n):
            if twoD_arr[i][j] == "":
                while alphabets[y] in key_set or alphabets[y] == "j":
                    y += 1
                twoD_arr[i][j] = alphabets[y]
                key_set.add(alphabets[y])
                y += 1

    # Display the 2D array
    for row in twoD_arr:
        print(row)

    message_current = message
    for i in range(len(message_current) - 1):
        if (
            message_current[i] == message_current[i + 1]
            and message_current[i] != "z"
            and message_current[i] != "x"
        ):
            message_current = message_current[: i + 1] + "z" + message_current[i + 2 :]

    decrypted = ""
    it1 = 0
    it2 = 1
    while it2 < len(message_current):
        letter1 = message_current[it1]
        letter2 = message_current[it2]
        index1, index2, index3, index4 = None, None, None, None

        # Find indices for the letters in the Playfair matrix
        for i in range(n):
            for j in range(n):
                if twoD_arr[i][j] == letter1:
                    index1, index2 = i, j
                if twoD_arr[i][j] == letter2:
                    index3, index4 = i, j

        # Case 1 - When both are in the same column
        if index2 == index4:
            decrypted += twoD_arr[(index1 - 1) % n][index2] + twoD_arr[(index3 - 1) % n][index4]

        # Case 2 - When both are in the same column
        elif index1 == index3:
            decrypted += twoD_arr[index1][(index2 - 1) % n] + twoD_arr[index3][(index4 - 1) % n]

        # Case 3 - when both are away from each other
        else:
            decrypted += twoD_arr[index1][index4] + twoD_arr[index3][index2]
        print(message_current[it1], message_current[it2])
        it1 += 2
        it2 += 2

    print(decrypted)
    return decrypted


def main():
    encrypted_message = playfair_encryption("DevPipalia", "Tiwari")
    decrypted_message = playfair_decryption(encrypted_message, "Tiwari")

main()
