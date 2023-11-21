import socket

def majority_bit(x, y, z):
    if x + y + z > 1:
        return 1
    else:
        return 0


def rightRotate(lists, num):
    output_list = []
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list

def leftRotate(lists, num):
    output_list = []
    for item in range(num, len(lists)):
        output_list.append(lists[item])

    for item in range(0, num):
        output_list.append(lists[item])

    return output_list


def a51_keystream():
    session_key = ""
    while len(session_key) != 8:
        session_key = input("Enter the session key (8-bit): ")
    
    x = [0] * 19
    y = [0] * 22
    z = [0] * 23

    for i in range(len(session_key)):
        x[0] = x[13] ^ x[16] ^ x[17] ^ x[18] ^ int(session_key[i])
        y[0] = y[20] ^ y[21] ^ int(session_key[i])
        z[0] = z[7] ^ z[20] ^ z[21] ^ z[22] ^ int(session_key[i])
        x = rightRotate(x, 1)
        y = rightRotate(y, 1)
        z = rightRotate(z, 1)
    
    keystream = ""
    for i in range(0,8):
        maj_bit = majority_bit(x[8],y[10],z[10])
        keystream += str(x[19]^y[21]^z[22]^maj_bit)
    
    print(keystream)
    return keystream

def encyption_decryption(message,keystream):
    encrypted = ""
    for i in range(len(message)):
        encrypted += str(int(message[i]) ^ int(keystream[i%len(keystream)]))
    return encrypted

def socket_function():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((socket.gethostname(),1234))
    print("Connection established")
    while True:
        message = "01010101"
        print(f"Message: {message}")
        # keystream = a51_keystream()
        keystream = '00110101'
        encrypted_message = encyption_decryption(message,keystream)
        print(f"Encypted Message: {encrypted_message}")
        client_socket.send(encrypted_message.encode('utf-8'))
        print("Message sent")
        client_socket.close()
        break

socket_function()


