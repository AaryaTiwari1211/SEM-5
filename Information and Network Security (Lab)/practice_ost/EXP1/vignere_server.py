import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))
server_socket.listen()

# Text - AaryaDhruv123
# Key - Dhariya

# A - 0 , B - 1 , C  - 2 ... Z - 25
# 0 + 3 mod 26 - 3

# Text - AaryaDhruv123
#Key -   DhairyaDhariy

def vignere_cipher_decryption(text,key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k = 0
    encrypted = ''
    for i in range(len(text)):
        if text[i].isupper():
            encrypted+=upper_alphabets[(upper_alphabets.find(text[i])-upper_alphabets.find(key[i%len(key)])) % len(upper_alphabets)]
        else:
            encrypted+=alphabets[(alphabets.find(text[i])-alphabets.find(key[i%len(key)])) % len(alphabets)]
            
    return encrypted

clientSocket , address = server_socket.accept()
print(f"Connection established as address {address}")

while True:
    message = clientSocket.recv(2048).decode('utf-8')
    print(f"Encrypted message: {message}")
    key = 'Aarya'
    if not message:
        break
    decrypted_message = vignere_cipher_decryption(message,key)
    print(f"Decrypted Message is: {decrypted_message}")
    break
clientSocket.close()
server_socket.close()

