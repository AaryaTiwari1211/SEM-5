import socket
import math
from random import randint


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def primitive_check(g, p):
    L = []
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return False
        return True


def generate_prime_and_primitive_root():
    while True:
        P = randint(0, 100)  # You can adjust the range as needed
        if is_prime(P):
            break

    while True:
        G = randint(2, P - 1)
        if primitive_check(G, P):
            break

    return P, G

def diffie_hellman_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 1234))
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    P, G = generate_prime_and_primitive_root()
    client_socket.send(f"{P},{G}".encode())
    x1 = int(input("Enter the private key of A: "))
    y1 = pow(G, x1, P)
    client_socket.send(str(y1).encode())
    y2 = int(client_socket.recv(1024).decode())
    k1 = pow(y2, x1, P)
    print(f"Key exchanged successfully! Shared key: {k1}")
    server_socket.close()

diffie_hellman_server()
