def mod_exp(generator, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * generator) % modulus
        generator = (generator * generator) % modulus
        exponent //= 2
    return result

def calculate_modular_exponentiation(q, a, p):
    a_star = pow(q, a, p)
    return a_star

def diffie_hellman():
    #Prime number and generator are common to both Alice and Bob
    prime = 7237
    generator = 26 

    #Alice and Bob's private keys are known only to them
    alice_private_key = 5356
    bob_private_key = 1813
    
    #Alice and Bob's public keys are calculated using their private keys
    alice_public_key = calculate_modular_exponentiation(generator, alice_private_key, prime)
    print("Alice's public key:", alice_public_key)
    bob_public_key = calculate_modular_exponentiation(generator, bob_private_key, prime)
    print("Bob's public key:", bob_public_key)
    
    #Alice and Bob's shared secret is calculated using their private keys and the other's public key
    alice_shared_secret = calculate_modular_exponentiation(bob_public_key, alice_private_key, prime)
    bob_shared_secret = calculate_modular_exponentiation(alice_public_key, bob_private_key, prime)

    return alice_shared_secret, bob_shared_secret

alice_shared_secret, bob_shared_secret = diffie_hellman()

print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)
