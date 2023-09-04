import random

def calculate_generator(p):
    for g in range(2, p):
        if pow(g, p - 1, p) == 1:
            return g

def diffie_hellman_key_exchange(p, g, a, RB):
    RA = pow(g, a, p)
    KAB = pow(RB, a, p)

    return RA, KAB

def xor_encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_char = chr(ord(message[i]) ^ key)
        encrypted_message += encrypted_char
    return encrypted_message

def calculate_modular_exponentiation(q, a, p):
    a_star = pow(q, a, p)
    return a_star


def xor_decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_char = chr(ord(encrypted_message[i]) ^ key)
        decrypted_message += decrypted_char
    return decrypted_message

def diffie_hellman():
    prime = 7297
    generator = calculate_generator(prime)
    print("Generator:", generator)
    
    alice_private_key = random.randint(1, prime-1)
    bob_private_key = random.randint(1, prime-1)
    
    print("Alice's private key:", alice_private_key)
    print("Bob's private key:", bob_private_key)
    
    alice_public_key = calculate_modular_exponentiation(generator, alice_private_key, prime)
    print("Alice's public key:", alice_public_key)
    bob_public_key = calculate_modular_exponentiation(generator, bob_private_key, prime)
    print("Bob's public key:", bob_public_key)

    alice_shared_secret = calculate_modular_exponentiation(bob_public_key, alice_private_key, prime)
    bob_shared_secret = calculate_modular_exponentiation(alice_public_key, bob_private_key, prime)

    return alice_shared_secret, bob_shared_secret

alice_shared_secret, bob_shared_secret = diffie_hellman()

print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)

# Message to be sent from Alice to Bob
message = "Hey bro my name is Aarya"

# Encrypt the message using XOR encryption and Alice's shared secret
encrypted_message = xor_encrypt(message, alice_shared_secret)

print("Encrypted message:", encrypted_message)

# Decrypt the message using XOR decryption and Bob's shared secret
decrypted_message = xor_decrypt(encrypted_message, bob_shared_secret)

print("Decrypted message:", decrypted_message)