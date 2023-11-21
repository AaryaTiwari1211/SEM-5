import socket

def diffie_hellman_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((socket.gethostname(), 1234))

    P, G = map(int, client_socket.recv(1024).decode().split(','))
    print(f"Received P: {P}, G: {G}")

    x2 = int(input("Enter the private key of B: "))
    y2 = pow(G, x2, P)
    client_socket.send(str(y2).encode())

    y1 = int(client_socket.recv(1024).decode())

    k2 = pow(y1, x2, P)
    print(f"Key exchanged successfully! Shared key: {k2}")

    client_socket.close()

diffie_hellman_client()