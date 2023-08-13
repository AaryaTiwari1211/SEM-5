def multiplicative_encryption(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_uppercase = char.isupper()
            char_idx = ord(char.upper()) - ord('A')
            encrypted_idx = (char_idx * key) % 26
            encrypted_char = chr(encrypted_idx + ord('A'))
            ciphertext += encrypted_char if is_uppercase else encrypted_char.lower()
        else:
            ciphertext += char
    
    print("Verification complete!! encrypted text is: ", ciphertext)

    return ciphertext

def multiplicative_decryption(ciphertext, key):
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    inverse_key = mod_inverse(key, 26)
    if inverse_key is None:
        raise ValueError(
            "Key does not have a modular inverse. It must be coprime with 26.")

    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_uppercase = char.isupper()
            char_idx = ord(char.upper()) - ord('A')
            decrypted_idx = (char_idx * inverse_key) % 26
            decrypted_char = chr(decrypted_idx + ord('A'))
            decrypted_text += decrypted_char if is_uppercase else decrypted_char.lower()
        else:
            decrypted_text += char
            
    print("Verification complete!! decrypted text is: ", decrypted_text)

    return decrypted_text


def additive_encryption(text, key):
    cipher = ""
    for letter in text:
        if letter.isupper():
            l = ord(letter) + key
            if l > 90:
                l = 65 + (l - 91)
            cipher += chr(l)
        else:
            l = ord(letter) + key
            if l > 122:
                l = 97 + (l - 123)
            cipher += chr(l)
    text1 = ""
    for letter in cipher:
        if letter.isupper():
            l = ord(letter) - key
            if l < 65:
                l = 91 - (65 - l)
            text1 += chr(l)
        else:
            l = ord(letter) - key
            if l < 97:
                l = 123 - (97 - l)
            text1 += chr(l)
    if text == text1:
        print("Verification complete!! encrypted text is: ", cipher)
        print(cipher)
    else:
        print("Incorrect Cipher")
        print(cipher)
        print(text)
        print(text1)


def additive_decryption(cipher, key):
    text = ""
    for letter in cipher:
        if letter.isupper():
            l = ord(letter) - key
            if l < 65:
                l = 91 - (65 - l)
            text += chr(l)
        else:
            l = ord(letter) - key
            if l < 97:
                l = 123 - (97 - l)
            text += chr(l)
    cipher1 = ""
    for letter in text:
        if letter.isupper():
            l = ord(letter) + key
            if l > 90:
                l = 65 + (l - 91)
            cipher1 += chr(l)
        else:
            l = ord(letter) + key
            if l > 122:
                l = 97 + (l - 123)
            cipher1 += chr(l)
    if cipher == cipher1:
        print("Verification complete!! decrypted text is: ", text)
    else:
        print("Incorrect Text")


x = True
while (x):
    print("Enter 1 for Additive encryption \n")
    print("Enter 2 for Additive decryption \n")
    print("Enter 3 for Multiplicative encryption \n")
    print("Enter 4 for Multiplicative decryption \n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        text = input("Enter the text you want to encrypt: ")
        key = int(input("Enter your key: "))
        additive_encryption(text, key)
    elif choice == 2:
        text = input("Enter the text you want to decrypt: ")
        key = int(input("Enter your key: "))
        additive_decryption(text, key)
    elif choice == 3:
        text = input("Enter the text you want to decrypt: ")
        key = int(input("Enter your key: "))
        multiplicative_encryption(text, key)
    elif choice == 4:
        text = input("Enter the text you want to decrypt: ")
        key = int(input("Enter your key: "))
        multiplicative_decryption(text, key)
    elif choice == 5:
        x = False
    else:
        print("Please enter a valid input!!")
