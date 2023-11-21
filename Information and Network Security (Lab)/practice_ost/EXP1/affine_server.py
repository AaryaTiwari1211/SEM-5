import socket
import math

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))
server_socket.listen()


def affine_cipher_decryption(text, key1, key2):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted1 = ""

    if math.gcd(key2, 26) != 1:
        print("There is no inverse for this key!!")
        key_inverse = 1
    else:
        key_inverse = pow(key2, -1, 26)

    for i in range(len(text)):
        if text[i].isupper():
            decrypted1 += upper_alphabets[
                (upper_alphabets.find(text[i]) * key_inverse) % len(upper_alphabets)
            ]
        else:
            decrypted1 += alphabets[
                (alphabets.find(text[i]) * key_inverse) % len(alphabets)
            ]

    decrypted2 = ""
    for i in range(len(decrypted1)):
        if decrypted1[i].isupper():
            decrypted2 += upper_alphabets[
                (upper_alphabets.find(decrypted1[i]) - key1) % len(upper_alphabets)
            ]
        else:
            decrypted2 += alphabets[
                (alphabets.find(decrypted1[i]) - key1) % len(alphabets)
            ]

    return decrypted2


while True:
    clientSocket, address = server_socket.accept()
    message = clientSocket.recv(2048).decode("utf-8")
    key1 = 3
    key2 = 17
    decrypted_message = affine_cipher_decryption(message, key1, key2)
    print(f"Decrypted message is: {decrypted_message}")
    break

clientSocket.close()
server_socket.close()
