def majority(x, y, z):
    # Returns the majority bit
    return (x & y) | (x & z) | (y & z)


def clock(register, majority_bit):
    new_bit = register[18] ^ majority_bit
    register.pop()
    register.insert(0, new_bit)



def generate_keystream(key, num_bits):
    # Convert key to a list of integers
    R1 = [int(bit) for bit in key] + [0] * (19 - len(key))
    R2 = [0] * 22
    R3 = [0] * 23 
    keystream = []

    for _ in range(num_bits):
        majority_bit = majority(R1[8], R2[10], R3[10])
        if R1[8] == majority_bit:
            clock(R1, majority_bit)
        if R2[10] == majority_bit:
            clock(R2, majority_bit)
        if R3[10] == majority_bit:
            clock(R3, majority_bit)
        keystream_bit = R1[18] ^ R2[21] ^ R3[22]
        keystream.append(keystream_bit)

    return keystream


def encrypt_or_decrypt(data, keystream):
    return [str(int(data[i]) ^ keystream[i]) for i in range(len(data))]


def a51_encrypt(key, plaintext):
    keystream = generate_keystream(key, len(plaintext))
    encrypted = encrypt_or_decrypt(plaintext, keystream)
    return ''.join(encrypted)


def a51_decrypt(key, ciphertext):
    # Encryption and decryption are the same in a stream cipher
    return a51_encrypt(key, ciphertext)


def main():
    key = "1010101010101010101"
    plaintext = "1101101010101010101"

    ciphertext = a51_encrypt(key, plaintext)
    decrypted_text = a51_decrypt(key, ciphertext)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
