import socket 

def vignere_cipher_encryption(text,key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k = 0
    encrypted = ''
    for i in range(len(text)):
        if text[i].isupper():
            encrypted+=upper_alphabets[(upper_alphabets.find(text[i])+upper_alphabets.find(key[i%len(key)])) % len(upper_alphabets)]
        else:
            encrypted+=alphabets[(alphabets.find(text[i])+alphabets.find(key[i%len(key)])) % len(alphabets)]
    
    return encrypted

def socket_function():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((socket.gethostname(),1234))
    print("Connection established!!")
    
    while True:
        message = input("Enter the message you want to send: ")
        key = "Aarya"
        encrypted_message = vignere_cipher_encryption(message,key)
        client_socket.send(encrypted_message.encode('utf-8'))
        print("Message sent")
        client_socket.close()
        break

socket_function()