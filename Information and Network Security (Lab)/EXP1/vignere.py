def affine_encrypt(text, a, b):
    cleaned_text = text.upper().replace(' ', '')
    encrypted_chars = []
    for char in cleaned_text:
        if char.isalpha():
            char_idx = ord(char) - ord('A')
            encrypted_idx = (a * char_idx + b) % 26
            encrypted_char = chr(encrypted_idx + ord('A'))
            encrypted_chars.append(encrypted_char)
    encrypted_text = ''.join(encrypted_chars)
    return encrypted_text

def affine_decrypt(cipher, a, b):
    a_inv = pow(a, -1, 26)

    decrypted_chars = []
    for char in cipher:
        if char.isalpha():
            char_idx = ord(char) - ord('A')
            decrypted_idx = (a_inv * (char_idx - b)) % 26
            decrypted_char = chr(decrypted_idx + ord('A'))
            decrypted_chars.append(decrypted_char)
    decrypted_text = ''.join(decrypted_chars)
    return decrypted_text


def vigenere_encrypt(text, key):
    key = key.upper()

    encrypted_chars = []
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % len(key)]
            shift = (ord(char) + ord(key_char) - 2 * ord('A')) % 26
            encrypted_char = chr(shift + ord('A'))
            encrypted_chars.append(encrypted_char)
        else:
            encrypted_chars.append(char)
    encrypted_text = ''.join(encrypted_chars)
    return encrypted_text


def vigenere_decrypt(cipher, key):
    key = key.upper()

    decrypted_chars = []
    for i in range(len(cipher)):
        char = cipher[i]
        if char.isalpha():
            key_char = key[i % len(key)]
            reverse_shift = (ord(char) - ord(key_char) + 26) % 26
            decrypted_char = chr(reverse_shift + ord('A'))
            decrypted_chars.append(decrypted_char)
        else:
            decrypted_chars.append(char)
    decrypted_text = ''.join(decrypted_chars)
    return decrypted_text


# text = input("Please enter text: ")
# a = int(input("Please enter first key for Affine cipher: "))
# b = int(input("Please enter second key for Affine cipher: "))
# affine_key = (a, b)
# vigenere_key = input("Please enter key for Vigenere cipher: ")
# affine_cipher = affine_encrypt(text, affine_key)
# vigenere_cipher = vigenere_encrypt(text, vigenere_key)
# print(affine_cipher)
# print(vigenere_cipher)
# affine_plain = affine_decrypt(affine_cipher, affine_key)
# vigenere_plain = vigenere_decrypt(vigenere_cipher, vigenere_key)
