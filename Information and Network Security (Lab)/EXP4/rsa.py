import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    while phi:
        quotient = e // phi
        e, phi = phi, e % phi
        x1, x2 = x2 - quotient * x1, x1
        y1, y2 = y2 - quotient * y1, y1
    d = x2
    return d

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = multiplicative_inverse(e, phi)
    
    return ((n, e), (n, d))

def encrypt(public_key, message):
    n, e = public_key
    encrypted = []

    for char in message:
        char_value = ord(char)
        encrypted_value = pow(char_value, e, n)
        encrypted.append(encrypted_value)
    
    return encrypted

def decrypt(private_key, encrypted):
    n, d = private_key
    decrypted = []

    for encrypted_value in encrypted:
        char_value = pow(encrypted_value, d, n)
        decrypted_char = chr(char_value)
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

def main_menu():
    print("RSA Encryption and Decryption")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Quit")
    choice = int(input("Enter your choice: "))
    return choice

if __name__ == '__main__':
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)
    
    while True:
        choice = main_menu()
        
        if choice == 1:
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt(public_key, message)
            print("Encrypted message:", encrypted_message)
        elif choice == 2:
            encrypted_message = list(map(int, input("Enter the encrypted message values (comma-separated): ").split(',')))
            decrypted_message = decrypt(private_key, encrypted_message)
            print("Decrypted message:", decrypted_message)
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")
