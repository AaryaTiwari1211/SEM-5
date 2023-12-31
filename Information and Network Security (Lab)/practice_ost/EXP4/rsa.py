import math

def encrypt(public_key,message):
    n , e = public_key
    encrypted_value = pow(int(message), e, n)
    return encrypted_value

def decrypt(private_key, encrypted_value):
    n, d = private_key
    decrypted_value = pow(int(encrypted_value), d, n)
    return decrypted_value

def is_prime(p):
    if p<2:
        return False
    for i in range(2,math.isqrt(p)+1):
        if p%i==0:
            return False
    return True

def rsa_main():
    while True:
        p = int(input("Enter p: "))
        q = int(input("Enter q: "))
        
        if not is_prime(p) or not is_prime(q):
            print("Either p or q is not prime. Try again!!")
        else:
            break
    
    n = p*q
    phi = (p-1)*(q-1)
    e = 0
    for i in range(2,phi):
        if math.gcd(i,phi) == 1:
            e = i
            print(e)
            break
        else:
            continue
    
    if math.gcd(e,phi) != 1:
        return False
    
    d = pow(e, -1, phi)
    print(d)
    
    public_key = (n,e)
    private_key = (n,d)
    
    message = input("Enter the message: ")
    
    encrypted_text = encrypt(public_key,message)
    print(encrypted_text)
    decrypted_text = decrypt(private_key,encrypted_text)
    print(decrypted_text)
    return public_key , private_key

rsa_main()
# y = pow(x, -1, p)