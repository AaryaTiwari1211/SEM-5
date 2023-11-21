#include <iostream>
#include <cmath>
#include<bits/stdc++.h>

using namespace std;

int modinv(int a, int m)
{
    a = a % m;
    for (int i = 1; i < m; i++)
    {
        if ((a * i) % m == 1)
        {
            return i;
        }
    }
    return -1;
}

int power(int x, unsigned int y, int p)
{
    int res = 1; // Initialize result
    x = x % p;   // Update x if it is more than or
    // equal to p

    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y % 2 != 0)
        {
            res = (res * x) % p;
        }

        // y must be even now
        y = y / 2;
        x = (x * x) % p;
    }
    return res;
}

int main()
{
    int p, q;

    cout << "Enter prime no 1 :";
    cin >> p;
    cout << "Enter prime no 2 :";
    cin >> q;

    int n = p * q;
    int phi = (p - 1) * (q - 1);

    int e = 2;
    while (e < phi)
    {
        if (__gcd(e, phi) == 1)
        {
            break;
        }
        else
        {
            e++;
        }
    }
    cout << "Public Key (e): " << e << endl;

    int d = modinv(e, phi);
    cout << "Private Key (d): " << d << endl;

    int m;
    cout << "Enter value of m: ";
    cin >> m;

    // Encryption
    int c = power(m, e, n);

    // Decryption
    int msg = power(c, d, n);

    cout << "Encrypted Message (c): " << c << endl;
    cout << "Decrypted Message: " << msg << endl;

    return 0;
}