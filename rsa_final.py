def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def modinv(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_encrypt_decrypt():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = int(input("Enter encryption key e: "))
    while gcd(e, phi) != 1:
        e = int(input("Enter valid e (co-prime with φ): "))
    d = modinv(e, phi)
    print(f"Public Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")

    msg = int(input("Enter message to encrypt (as number < n): "))
    encrypted = pow(msg, e, n)
    decrypted = pow(encrypted, d, n)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

rsa_encrypt_decrypt()
