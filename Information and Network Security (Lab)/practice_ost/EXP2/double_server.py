import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),1234))
server_socket.listen()


def columnar_decrypt(text, key):
    max_ = max(key)
    rows, cols = (max_ + 1, max_ + 1)
    arr = [["x" for i in range(cols)] for j in range(rows)]
    x = 0
    for i in range(rows):
        for j in range(cols):
            arr[j][i] = text[x]
            x = x + 1
    print(arr)
    decrypted = ""
    for i in range(len(arr[i])):  # [0,3,2,1]
        for j in key:
            decrypted += arr[i][j]
    print(decrypted)
    return decrypted

def row_decrypt(text, key):
    max_ = max(key)
    rows, cols = (max_ + 1, max_ + 1)
    arr = [["x" for i in range(cols)] for j in range(rows)]
    x = 0
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = text[x]
            x = x + 1
    decrypted = ""
    arr_2 = arr.copy()

    for i in range(len(key)):
        arr_2[int(key[i])] = arr[i]
    
    for i in range(rows):
        for j in range(cols):
            decrypted += arr_2[i][j]
            x = x + 1
    print(decrypted)
    return decrypted

while True:
    clientSocket , address = server_socket.accept()
    message = clientSocket.recv(2048).decode('utf-8')
    key1 = [0,3,2,1]
    key2 = [0,2,1,3]
    decryption1 = columnar_decrypt(message,key2)
    decryption2 = row_decrypt(decryption1,key1)
    print(f"Decrypted Message is: {decryption2}")
    break

clientSocket.close()
server_socket.close()