def elgamal():
    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))
    x = int(input("Enter private key x: "))
    y = pow(g, x, p)

    k = int(input("Enter random key k: "))
    m = int(input("Enter message (as integer): "))

    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    print("Encrypted Pair (c1, c2):", (c1, c2))

    decrypted = (c2 * pow(c1, p - 1 - x, p)) % p
    print("Decrypted Message:", decrypted)

elgamal()