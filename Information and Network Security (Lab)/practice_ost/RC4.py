import math

n = 256

def int_converter(arr):
    arr = arr.split()
    arr = list(map(int,arr))
    return arr

def key_scheduling(S,key):
    j = 0
    T = []
    for i in range(len(S)):
        T.append(key[i%len(key)])
    print(T)
    for i in range(n):
        j = math.fmod(j + S[i] + T[i],n)
        j = int(j)
        S[i] , S[j] = S[j] , S[i]
    print(S)
    return S

def pseudo_random(S,key):
    i= 0
    j = 0
    K = []
    for k in range(len(key)):
        i = (i+1)%n
        j = (j+S[i])%n
        S[i] , S[j] = S[j],S[i]
        t = (S[i] + S[j])%n
        K.append(S[t])
    return K

def encryption(keystream,plaintext):
    ciphertext = []
    for i in range(len(keystream)):
        ciphertext.append(int(keystream[i])^int(plaintext[i])) 
    return ciphertext

def decryption(keystream,ciphertext):
    return encryption(keystream,ciphertext)

def main():
    S = [i for i in range(n)]
    print(S)
    plain_text = input("Enter the plaintext (with spaces): ")
    key = input("Enter the key (With spaces): ")
    key = int_converter(key)
    plain_text = int_converter(plain_text)
    S_1 = key_scheduling(S,key,plain_text)
    keystream = pseudo_random(S_1,key)
    print(keystream)
    ciphertext = encryption(keystream,plain_text)
    print(ciphertext)
    plain_text = decryption(keystream,ciphertext)
    print(plain_text)

main()