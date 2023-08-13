def multiplicative_cipher_encrypt(plaintext, key):
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

    return ciphertext

def multiplicative_cipher_decrypt(ciphertext, key):
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

    return decrypted_text


# Example usage
plaintext = "HELLO WORLD"
key = 7
encrypted_text = multiplicative_cipher_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = multiplicative_cipher_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
