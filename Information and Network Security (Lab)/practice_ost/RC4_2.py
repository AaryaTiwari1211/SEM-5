import math
n = 256
S = [i for i in range(n)]
def key_scheduling(S,key):
    print(f"S matrix is: {S}")
    print(f"Key matrix is: {key}")
    T = [key[i%len(key)] for i in range(len(S))]
    print(f"T matrix is: {T}")
    
    j = 0
    for i in range(len(S)):
        j = (j+S[i]+T[i])%n
        S[i],S[j] = S[j],S[i]
    
    return S

def pseudo_random_key(S,key):
    i = 0
    j = 0
    k = 0
    K = []
    while k!=len(key):
        i = (i+1)%n
        j = (j+S[i])%n
        S[i],S[j] = S[j],S[i]
        t = (S[i] + S[j])%n
        key_item = S[t]
        K.append(key_item)
    
    return K

