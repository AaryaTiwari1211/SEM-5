import sympy
import random
l = 100
h = 1000


def modular_inverse(a, m):
    g, x, y = sympy.gcdex(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m


def prime_number_gen(l, h):
    prime_numbers = list(sympy.primerange(l, h+1))

    p1 = random.choice(prime_numbers)
    p2 = random.choice(prime_numbers)
    return p1, p2


def euler_totient(p, q):
    return (p-1)*(q-1)


def e_calculator(fi):
    while True:
        e = random.randint(2, fi - 1)
        if sympy.gcd(e, fi) == 1:
            return e


def d_calculator(e, fi):
    return modular_inverse(e, fi)


# def public_key_gen(e, n):
#     public_key = (e, n)
#     return public_key

def public_key_gen(p, q):
    n = p * q
    fi = euler_totient(p, q)
    e = 65537
    return e, n


def private_key_gen(d, n):
    private_key = (d, n)
    return private_key


def encryptor(public_key, message):
    e, n = public_key
    encrypted_message = message**e % n
    return encrypted_message


def decryptor(private_key, encrypted_message):
    d, n = private_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message


def main():
    # p, q = prime_number_gen(l, h)
    p = 103
    q = 127
    n = p * q
    fi = euler_totient(p, q)

    # Choose a fixed value for e, such as 65537
    e = 65537

    # Calculate the modular inverse of e with respect to fi
    d = modular_inverse(e, fi)

    public_key = public_key_gen(e, n)
    private_key = private_key_gen(d, n)

    message = int(input("Enter the message: "))
    encrypted_message = encryptor(public_key, message)
    decrypted_message = decryptor(private_key, encrypted_message)

    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)


main()
