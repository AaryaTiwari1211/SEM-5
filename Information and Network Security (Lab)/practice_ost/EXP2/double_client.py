import socket

def columnar_encrypt(text, key):
    text_length = len(text)
    max_ = max(key)
    rows, cols = (max_ + 1, max_ + 1)
    arr = [["x" for i in range(cols)] for j in range(rows)]
    x = 0
    for i in range(rows):
        for j in range(cols):
            if x >= text_length:
                arr[i][j] = "_"
            else:
                arr[i][j] = text[x]
                x = x + 1
    encrypted = ""
    for i in key:  # [1,3,2,0]
        for j in range(len(arr[i])):  # [0,1,2,3]
            encrypted += arr[j][i]
    return encrypted


def row_encrypt(text, key):
    text_length = len(text)
    max_ = max(key)
    rows, cols = (max_ + 1, max_ + 1)
    arr = [["x" for i in range(cols)] for j in range(rows)]
    x = 0
    for i in range(rows):
        for j in range(cols):
            if x >= text_length:
                arr[i][j] = "_"
            else:
                arr[i][j] = text[x]
                x = x + 1
    encrypted = ""
    for i in key:
        for j in range(len(arr[j])):  # [1,3,2,0]
            encrypted += arr[i][j]
    return encrypted

def socket_function():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((socket.gethostname(),1234))
    print("Connecttion established!!")
    while True:
        message = input("Enter the message you want to send: ")
        key1 = [0,3,2,1]
        key2 = [0,2,1,3]
        encryption1 = row_encrypt(message,key1)
        encryption2 = columnar_encrypt(encryption1,key2)
        print(f"Encrypted Text = {encryption2}")
        client_socket.send((encryption2.encode('utf-8')))
        print("Message sent")
        break

socket_function()