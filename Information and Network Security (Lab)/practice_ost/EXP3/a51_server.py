import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),1234))
server_socket.listen()
clientSocket , address = server_socket.accept()
print(f"Server running at address {address}")

def encyption_decryption(message,keystream):
    encrypted = ""
    for i in range(len(message)):
        encrypted += str(int(message[i]) ^ int(keystream[i%len(keystream)]))
    return encrypted

while True:
    message = clientSocket.recv(2048).decode('utf-8')
    print(f"Encrypted message: {message}")
    keystream = '00110101'
    decrypted_message = encyption_decryption(message,keystream)
    print(f"Decrypted Message: {decrypted_message}")
    break

clientSocket.close()
server_socket.close()

