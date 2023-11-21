import socket


def affine_cipher_encryption(text, key1, key2):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    for i in range(len(text)):
        if text[i].isupper():
            encrypted += upper_alphabets[
                (upper_alphabets.find(text[i]) + key1) % len(upper_alphabets)
            ]
        else:
            encrypted += alphabets[(alphabets.find(text[i]) + key1) % len(alphabets)]

    encrypted2 = ""
    for i in range(len(encrypted)):
        if encrypted[i].isupper():
            encrypted2 += upper_alphabets[
                (upper_alphabets.find(encrypted[i]) * key2) % len(upper_alphabets)
            ]
        else:
            encrypted2 += alphabets[(alphabets.find(encrypted[i]) * key2) % len(alphabets)]
    return encrypted2


def socket_function():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((socket.gethostname(), 1234))
    print("Connection established!!")

    while True:
        message = input("Enter the message you want to send: ")
        print(f"Message is: {message}")
        key1 = 3
        key2 = 17
        encrypted_message = affine_cipher_encryption(message,key1,key2)
        print(f"Encrypted message is: {encrypted_message}")
        client_socket.send(encrypted_message.encode("utf-8"))
        print("Message sent")
        client_socket.close()
        break


socket_function()
