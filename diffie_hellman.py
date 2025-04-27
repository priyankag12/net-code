def diffie_hellman():
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a primitive root g: "))
    a = int(input("Enter Alice's private key: "))
    b = int(input("Enter Bob's private key: "))

    A = pow(g, a, p)
    B = pow(g, b, p)

    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    print("Shared Key (Alice):", key_A)
    print("Shared Key (Bob):", key_B)
    print("Key exchange complete!")

diffie_hellman()
